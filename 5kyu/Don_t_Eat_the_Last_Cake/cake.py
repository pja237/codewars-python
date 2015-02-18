#!/usr/bin/python

bcache=dict()
blist=list()

def sim(cakes,last,choices):
    global bcache
    branch_score=0
    print "-----"
    print "*Entered sim:",cakes, last
    if cakes==1 or (cakes==2 and last==1):
        print "LAST CAKE! <=> this branch is a loss, substract -1 from branch score"
        print "--- EO-subtree ---"
        bcache[str(cakes)+'-'+str(last)]=-1
        return -1
    elif cakes<=0:
        print "WIN SITUATION <=> this branch is a win, add 1 to branch score"
        print "--- EO-subtree ---"
        bcache[str(cakes)+'-'+str(last)]=1
        return 1
    else:
        tmp=sorted( list(set(choices)-{last}) )
        print "tmp=",tmp
        branch_score=sim(cakes-tmp[0], tmp[0], choices)+sim(cakes-tmp[1], tmp[1], choices)
    print "branch",cakes, last," score == ", branch_score
    bcache[str(cakes)+'-'+str(last)]=branch_score
    blist.append([str(cakes)+'-'+str(last), branch_score])
    return branch_score

S=[1,2,3]
cakes=5

for i in S:
    print sim(cakes-i,i,S)
print bcache
print blist
