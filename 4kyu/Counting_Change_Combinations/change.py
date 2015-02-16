#!/usr/bin/python

change_combs=list()
#change_combs=0

def recurse_change(count, way, total, denoms):
    #print " count, way, total, denoms ",count, way, total, denoms 
    #print " change_combs ", change_combs
    #raw_input()
    if count==total:
        if not sorted(way) in change_combs: change_combs.append(sorted(way))
    elif count<total:
        for i in denoms:
            recurse_change(count+i, way+[i], total, denoms)
    return 0

l_counter=0

def iter_change(node, way, total, denoms):
    global l_counter
    change_combs=0
    stack=list()
    sumway=[sum(way)]
    stack.append(filter(lambda i: (sum(way)+i)<=total and i>node, denoms))
    #stack=[['x']]
    #print node, way, total, denoms, stack
    #while stack[0]:
    while True:
        s=sumway[-1]
        #print "IN  N",node,"T",total,"S",stack,"W",way,"C",change_combs,"SUM",s,"SUMWAY",sumway
        if s<total:
            way+=[node]
            sumway+=[sum(way)]
            #stack.append(filter(lambda i: (sum(way)+i)<=total and i!=node, denoms)[::-1])
            stack.append(filter(lambda i: (sum(way)+i)<=total and i>node, denoms))
        else:
            #if s==total: change_combs.append(way)
            if s==total: 
                print way
                change_combs+=1
            while stack and not stack[-1]:
                sumway=sumway[:-1]
                way=way[:-1]
                stack=stack[:-1]
            if not stack: break
            node=stack[-1][0]
            stack[-1].remove(node)
            #print "STACK CLEANUP  N",node,"T",total,"S",stack,"W",way,"C",change_combs,"SUM",s,"SUMWAY",sumway

        #print "OUT  N",node,"T",total,"S",stack,"W",way,"C",change_combs,"SUM",s,"SUMWAY",sumway
        #raw_input()
        l_counter+=1
        if node=='x': break
    return change_combs

def count_change(n, d):
    global l_counter
    l_counter=0
    #global change_combs
    #change_combs=[]
    c=0
    i=0
    d=sorted(d)
    while i<len(d):
        #c+=recurse_change(d[i],[d[i]],n,d[i:])
        c+=iter_change(d[i], [d[i]], n, d[i:])
        i+=1
    print " LOOPS TO CALCULATE:", l_counter
    #print " FINAL change_combs ", change_combs
    #return len(change_combs)
    return c
    

print "10 [1,2,5] ",count_change(10, [1,2,5]) # => 3
print "4 /2 ",count_change(4, [1,2]) # => 3
print "10/3",count_change(10, [5,2,3]) # => 4
exit()
#print count_change(11, [5,7]) # => 0
print "20 / 3",count_change(20, [1,2,3]) # => 0
print " 50/3 ",count_change(50, [1,2,3]) # => 0
print " -- "
print " 50 / 10",count_change(50, [1,2,3,4,5,6,7,8,9,10]) # => 0
print " 100 / 2",count_change(100, [1,2]) # => 0
print " 100 / 4",count_change(100, [1,2,3,4]) # => 0
print " 100 / 6",count_change(100, [1,2,3,4,5,6]) # => 0
