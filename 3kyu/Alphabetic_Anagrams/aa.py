#!/usr/bin/python

import math

def aa(word):
    result=0
    P=lambda W: math.factorial(len(W))/reduce(lambda i,j: i*math.factorial(W.count(j)), set(W),1)

    s_word=''.join(sorted(word))
    w=word
    s_w=s_word
    for i in xrange(len(word)):
        print "word=",w
        print "sorted:",s_w
        #print "Letter:",i,'=',word[i]
        #print "Distance to first letter:",list(s_w).index(word[i])
        #print "Distance to first letter:",sorted(list(set(s_w))).index(word[i])
        #print "Letters to permute:",sorted(list(set(s_w)))[:sorted(list(set(s_w))).index(word[i])]
        #print "Total number of permutations:"
        #for j in s_w[:list(s_w).index(word[i])]:
        for j in sorted(list(set(s_w)))[:sorted(list(set(s_w))).index(word[i])]:
            tmp=list(s_w)
            #print " x ",j,tmp
            tmp.remove(j)
            #print j,'permutations:',tmp,'==',P(''.join(tmp))
            result+=P(''.join(tmp))

        tmp=list(s_w)
        tmp.remove(word[i])
        s_w=''.join(tmp)

        tmp=list(w)
        tmp.remove(word[i])
        w=''.join(tmp)
        #print "---"
    return result+1
        

def aal(word):
    result=0
    P=lambda W: math.factorial(len(W))/reduce(lambda i,j: i*math.factorial(W.count(j)), set(W),1)

    w=list(word)
    s_w=sorted(word)
    for i in xrange(len(word)):
        for j in sorted(list(set(s_w)))[:sorted(list(set(s_w))).index(word[i])]:
            tmp=s_w[:]
            tmp.remove(j)
            result+=P(''.join(tmp))

        s_w.remove(word[i])
        w.remove(word[i])

    return result+1





print "--------------------------------------------------------------------------------"
print aal('ABAB') , 2
print aal('AAAB') , 1
print aal('BAAA') , 4
print aal('CBDA')
print aal('QUESTION') , 24572
print aal('BOOKKEEPER') , 10743
