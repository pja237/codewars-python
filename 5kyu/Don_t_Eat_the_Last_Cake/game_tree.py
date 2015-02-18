#!/usr/bin/python

class Node:
    def __init__(self, n, l, pl, w='D'):
        self.number=n
        self.last=l
        self.player=pl
        self.wins=w
        self.Left=None
        self.Right=None

# build_tree(number of cakes, no. of last taken, player turn, Set)
def build_tree(n, l, pt, S):
    print "build:",n,l,pt
    if n<=0:
        return None
    else:
        print " -> make node, go down"
        tmp=sorted(list(set(S)-{l}))
        print tmp
        x=Node(n,l,pt)
        next_player=1 if pt==2 else 2
        x.Left=build_tree(n-tmp[0], tmp[0], next_player, S)
        x.Right=build_tree(n-tmp[1], tmp[1], next_player, S)
        if n-tmp[0]<=0 and n-tmp[1]<=0: x.wins=pt
        return x

def go_tree(node):
    if node==None: 
        print "---"
        return
    print "@ Node:",node.number, node.last, node.player, node.wins
    go_tree(node.Left)
    print "@ Node:",node.number, node.last, node.player, node.wins
    go_tree(node.Right)
    return

def make_wins(node):
    if node==None:
        return 0
    print "Node",node.number
    wl=make_wins(node.Left)
    wr=make_wins(node.Right)
    next_pl=1 if node.player==2 else 2
    if wl==wr==0:
        node.wins=node.player
    elif next_pl in (wl,wr):
        node.wins=next_pl
    else:
        node.wins=node.player

    return node.wins


N=8
S=[1,2,3]
Start_player=1

tree1=build_tree(N-1, 1, Start_player, S)
tree2=build_tree(N-2, 2, Start_player, S)
tree3=build_tree(N-3, 3, Start_player, S)
print " ----- "
print "Tree 1"
go_tree(tree1)
print "Tree 2"
go_tree(tree2)
print "Tree 3"
go_tree(tree3)

print "make wins 1"
make_wins(tree1)
go_tree(tree1)
print "make wins 2"
make_wins(tree2)
go_tree(tree2)
print "make wins 3"
make_wins(tree3)
go_tree(tree3)

print "Pl.",Start_player,"starts, PATH 1 wins:",tree1.wins
print "Pl.",Start_player,"starts, PATH 2 wins:",tree2.wins
print "Pl.",Start_player,"starts, PATH 3 wins:",tree3.wins
