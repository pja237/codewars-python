#!/usr/bin/python

import time
cache=dict()
count=0

class Player:
    def __init__(self, cakes):
        self.cakes=cakes
        self.tree1=None
        self.tree2=None
        self.tree3=None
        self.start=0
        self.trees=[self.tree1, self.tree2, self.tree3]
        self.intree=0
        self.atnode=None

    def dump(self):
        print 'cakes:',self.cakes
        print self.tree1
        print self.tree2
        print self.tree3
        print 'start order:',self.start
        print "TREE 1"
        self.go_tree(self.tree1)
        print "TREE 2"
        self.go_tree(self.tree2)
        print "TREE 3"
        self.go_tree(self.tree3)
    
    def firstmove(self, cakes): 
        S=[1,2,3]
        Start_player=1
        print "STOPWATCH START"
        t=time.time()
        self.tree1=self.build_tree(cakes-1, 1, Start_player, S)
        self.tree2=self.build_tree(cakes-2, 2, Start_player, S)
        self.tree3=self.build_tree(cakes-3, 3, Start_player, S)
        print "STOPWATCH END", time.time()-t
        print "STOPWATCH START"
        self.make_wins(self.tree1)
        self.make_wins(self.tree2)
        self.make_wins(self.tree3)
        print "STOPWATCH END", time.time()-t
        self.trees=[self.tree1, self.tree2, self.tree3]
        if Start_player in (self.tree1.wins if self.tree1 else -1, self.tree2.wins if self.tree2 else -1, self.tree3.wins if self.tree3 else -1):
            self.start=1
            return True
        else:
            self.start=2
            return False

    def move(self, cakes, last):
        if cakes==self.cakes:
            # choose a win-tree and go with it
            self.intree=(self.tree1.wins if self.tree1 else -1, self.tree2.wins if self.tree2 else -1, self.tree3.wins if self.tree3 else -1).index(self.start)
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
            print "@ tree:",self.intree
            print "@ cakes",self.atnode.number, self.atnode.last
            # pick next from tree and return
            if self.atnode.Left!=None and self.atnode.Left.wins==self.start:
                self.atnode=self.atnode.Left
                return self.atnode.last
            elif self.atnode.Right!=None and self.atnode.Right.wins==self.start:
                self.atnode=self.atnode.Right
                return self.atnode.last

    def build_tree(self, n, l, pt, S):
        global cache
        global count

        #count+=1
        if n<=0:
            return None

        tmp=sorted(list(set(S)-{l}))

        if not str(n)+'+'+str(l) in cache.keys():
            x=Node(n,l,pt)
            next_player=1 if pt==2 else 2
            x.Left=self.build_tree(n-tmp[0], tmp[0], next_player, S)
            x.Right=self.build_tree(n-tmp[1], tmp[1], next_player, S)
            if n-tmp[0]<=0 and n-tmp[1]<=0: x.wins=pt
            cache[str(n)+'+'+str(l)]=x

        return cache[str(n)+'+'+str(l)]

    def build_tree_x(self, n, l, pt, S):
        global count
        count+=1

        if n<=0:
            return None
        else:
            tmp=sorted(list(set(S)-{l}))
            x=Node(n,l,pt)
            next_player=1 if pt==2 else 2
            x.Left=self.build_tree(n-tmp[0], tmp[0], next_player, S)
            x.Right=self.build_tree(n-tmp[1], tmp[1], next_player, S)
            if n-tmp[0]<=0 and n-tmp[1]<=0: x.wins=pt
            return x

    def go_tree(self,node):
        if node==None:
            print "---"
            return
        print "@ Node:",node.number, node.last,'pl:', node.player, 'wins:', node.wins
        self.go_tree(node.Left)
        print "@ Node:",node.number, node.last,'pl:', node.player, 'wins:', node.wins
        self.go_tree(node.Right)
        return

    def make_wins(self,node):
        global count
        count+=1

        if node==None:
            return 0
        wl=self.make_wins(node.Left)
        wr=self.make_wins(node.Right)
        next_pl=1 if node.player==2 else 2
        if wl==wr==0:
            if node.number==node.last==1:
                # STALEMATE!!! OTHER PLAYER WINS
                node.wins=next_pl
            else:
                node.wins=node.player
        elif next_pl in (wl,wr):
            node.wins=next_pl
        else:
            node.wins=node.player
    
        return node.wins

class Node:
    def __init__(self, n, l, pl, w='D'):
        self.number=n
        self.last=l
        self.player=pl
        self.wins=w
        self.Left=None
        self.Right=None


N=30
pero=Player(N)
print pero.firstmove(N)
print count
print cache
#pero.dump()
