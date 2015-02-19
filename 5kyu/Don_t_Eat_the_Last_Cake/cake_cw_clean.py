#!/usr/bin/python

cache=dict()
cache_wins=dict()

class Player:
    def __init__(self, cakes):
        self.cakes=cakes
        self.tree1=None
        self.tree2=None
        self.tree3=None
        self.tree1_wins=0
        self.tree2_wins=0
        self.tree3_wins=0
        self.start=0
        self.trees=[self.tree1, self.tree2, self.tree3]
        self.intree=0
        self.atnode=None
    
    def firstmove(self, cakes): 
        global cache
        # Feeling dirty now... we're caching old game states to speed things up... a bit ashamed for "cheating" :S
        #cache={}
        #cache_wins={}
        #print "CACHE SIZE:",len(cache.keys())
        #print "CACHE_WINS SIZE:",len(cache_wins.keys())
        S=[1,2,3]
        Start_player=1
        self.tree1=self.build_tree_dp(cakes-1, 1, Start_player, S)
        self.tree2=self.build_tree_dp(cakes-2, 2, Start_player, S)
        self.tree3=self.build_tree_dp(cakes-3, 3, Start_player, S)
        self.tree1_wins=self.find_wins(self.tree1)
        self.tree2_wins=self.find_wins(self.tree2)
        self.tree3_wins=self.find_wins(self.tree3)
        self.trees=[self.tree1, self.tree2, self.tree3]
        
        if Start_player in (self.tree1_wins, self.tree2_wins, self.tree3_wins):
            self.start=1
            return True
        else:
            self.start=2
            return False

    def move(self, cakes, last):
        #print "move(",cakes, last,")"
        if cakes==self.cakes:
            # choose a win-tree and go with it
            self.intree=(self.tree1_wins, self.tree2_wins, self.tree3_wins).index(self.start)
            self.atnode=self.trees[self.intree]
            return self.atnode.last
        else:
            # find which tree opponent chose
            if self.atnode==None:
                self.intree=(self.tree1.number if self.tree1 else -1, self.tree2.number if self.tree2 else -1, self.tree3.number if self.tree3 else -1).index(cakes)
                self.atnode=self.trees[self.intree]
                
            if self.atnode.number==cakes:
                pass
            elif self.atnode.Left!=None and self.atnode.Left.number==cakes:
                self.atnode=self.atnode.Left
            elif self.atnode.Right!=None and self.atnode.Right.number==cakes:
                self.atnode=self.atnode.Right
            # pick next from tree and return
            if self.atnode.Left!=None and self.find_wins(self.atnode.Left)==self.start:
                self.atnode=self.atnode.Left
                return self.atnode.last
            elif self.atnode.Right!=None and self.find_wins(self.atnode.Right)==self.start:
                self.atnode=self.atnode.Right
                return self.atnode.last

    def build_tree_dp(self, n, l, pt, S):
        global cache

        if n<=0:
            return None

        tmp=sorted(list(set(S)-{l}))

        if not str(n)+'+'+str(l)+'+'+str(pt) in cache.keys():
            x=Node(n,l,pt)
            next_player=1 if pt==2 else 2
            x.Left=self.build_tree_dp(n-tmp[0], tmp[0], next_player, S)
            x.Right=self.build_tree_dp(n-tmp[1], tmp[1], next_player, S)
            if n-tmp[0]<=0 and n-tmp[1]<=0: x.wins=pt
            cache[str(n)+'+'+str(l)+'+'+str(pt)]=x

        return cache[str(n)+'+'+str(l)+'+'+str(pt)]

    def find_wins(self,node):

        if node==None:
            return 0
        wins=0

        if not str(node.number)+'+'+str(node.last)+'+'+str(node.player)+'+'+str(node.wins) in cache_wins.keys():
            wl=self.find_wins(node.Left)
            wr=self.find_wins(node.Right)
            next_pl=1 if node.player==2 else 2
            if wl==wr==0:
                if node.number==node.last==1:
                    # STALEMATE!!! OTHER PLAYER WINS
                    wins=next_pl
                else:
                    wins=node.player
            elif next_pl in (wl,wr):
                wins=next_pl
            else:
                wins=node.player
            cache_wins[str(node.number)+'+'+str(node.last)+'+'+str(node.player)+'+'+str(node.wins)]=wins

        return cache_wins[str(node.number)+'+'+str(node.last)+'+'+str(node.player)+'+'+str(node.wins)]


class Node:
    def __init__(self, n, l, pl, w='D'):
        self.number=n
        self.last=l
        self.player=pl
        self.wins=w
        self.Left=None
        self.Right=None

