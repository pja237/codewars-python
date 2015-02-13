#!/usr/bin/python

change_combs=list()

def recurse_change(count, way, total, denoms):
    #print " count, way, total, denoms ",count, way, total, denoms 
    #print " change_combs ", change_combs
    #raw_input()
    if count==total:
        if not sorted(way) in change_combs: change_combs.append(sorted(way))
    elif count<total:
        for i in denoms:
            recurse_change(count+i, way+[i], total, denoms)

def iterative_change(node, total, denoms):
    stack=list()
    way=list()
    while not stack or node!=0:
        print "IN  N",node,"T",total,"S",stack,"W",way,"C",change_combs
        if sum(way)>=total: node=0
        if node!=0:
            way+=[node]
            tmp=filter(lambda i: (sum(way)+i)<=total, denoms)
            print tmp
            stack+=tmp[1:]
            node=tmp[0] if tmp else denoms[0]
            #stack+=denoms[1:] if node==denoms[0] else ''
            #node=denoms[0]
        else:
            if sum(way)==total: change_combs.append(way)
            node=stack[-1]
            stack=stack[:-1]
            way=way[:-1]

        print "OUT N",node,"T",total,"S",stack,"W",way,"C",change_combs
        raw_input()
		



def count_change(n, d):
    global change_combs
    change_combs=[]
    i=0
    d=sorted(d)
    while i<len(d):
        recurse_change(d[i],[d[i]],n,d[i:])
        #iterative_change(d[i],n,d[i:])
        i+=1
    print " FINAL change_combs ", change_combs
    return len(change_combs)
    

print count_change(4, [1,2]) # => 3
print " Expected: 3"
print count_change(10, [5,2,3]) # => 4
print " Expected: 4"
print count_change(11, [5,7]) # => 0
print " Expected: 0"
print count_change(20, [1,2,3]) # => 0
