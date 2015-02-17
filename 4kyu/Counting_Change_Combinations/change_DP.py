#!/usr/bin/python

import time

c=0

memo=dict()

def mapkey(n, m):
    return '|'.join([str(n),str(m)])

def count_memo( n, m ):
    global c
    c+=1
    if n == 0:
        #print " => ONE solution here == SUM, returning 1"
        memo[mapkey(n,m)]=1
        return 1
    if n < 0:
        #print " => NO solutions here, wen't OVER the SUM, returning 0"
        return 0
    if m < 0 and n >= 1: 
        #print " => NO solutions here, ran out  of denominations to try, returning 0"
        return 0
 
    #print 'count(', n,',', m-1,') + count(', n - S[m],',', m,')'

    if not mapkey(n,m) in memo.keys():
        memo[mapkey(n,m)] = count_memo(n, m-1) + count_memo(n-S[m], m)

    return memo[mapkey(n,m)]

def count_nomemo( n, m ):
    global c
    c+=1
    if n == 0:
        #print " => ONE solution here == SUM, returning 1"
        return 1
    if n < 0:
        #print " => NO solutions here, wen't OVER the SUM, returning 0"
        return 0
    if m < 0 and n >= 1:
        #print " => NO solutions here, ran out  of denominations to try, returning 0"
        return 0

    #print 'count(', n,',', m-1,') + count(', n - S[m],',', m,')'

    return count_nomemo(n, m-1) + count_nomemo(n-S[m], m)




#N=100
#S=[1,2,3,4,5,6,7,8,9,10]

N=10
S=[5,2,3]

c=0
start=time.time()
print "NOMEMO"
print "N=",N,"DENOMS=",S
print "RESULT=",count_nomemo (N,len(S)-1)
print "Function calls:",c
print "TIME: ",time.time()-start
print
c=0
start=time.time()
print "MEMO"
print "N=",N,"DENOMS=",S
print "RESULT=",count_memo(N ,len(S)-1)
print "Function calls:",c
print "TIME: ",time.time()-start
print
