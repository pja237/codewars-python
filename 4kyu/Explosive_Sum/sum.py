#!/usr/bin/python

import time

cache=dict()
D=list()
count=0

def ckey(n,s):
    return str(n)+'|'+str(s)

cache_euler=dict()

def eulers_pentagonals(n):
    global cache_euler
    if n==0: return 1
    elif n<0: return 0

    if not n in cache_euler.keys():
        cache_euler[n]=sum(map(lambda i: int((-1)**(i-1))*eulers_pentagonals( n - i*(3*i-1)/2 ) , range(1,n+1)+range(-1,-n-1,-1)))

    return cache_euler[n]

def part_count(n, s):
    global cache
    global D
    global count
    count+=1
    if n==0:
        return 1
    elif n<0:
        return 0
    elif n>0 and s<0:
        return 0

    if not ckey(n,s) in cache.keys():
        cache[ckey(n,s)]=part_count(n, s-1) + part_count(n-D[s], n-D[s]-1 if D[s]>n/2 else s)

    return cache[ckey(n,s)]

def n_sum(n):
    global D
    global count
    count=0
    if n<0: return 0
    elif n==0: return 1
    D=range(1,n+1)
    return part_count(n, n-1)

t=time.time()
print n_sum(200)
print time.time()-t
t=time.time()
print eulers_pentagonals(200)
print time.time()-t

#print n_sum(-1) ,' 0'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#print n_sum(1) ,' 1'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#print n_sum(2) ,' 2  -> 1+1 , 2'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#print n_sum(3) ,' 3 -> 1+1+1, 1+2, 3'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#print n_sum(4) ,' 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#print n_sum(5) ,' 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#print n_sum(10) ,' 42'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#print n_sum(50) ,' 204226'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#print n_sum(80) ,' 15796476'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#print n_sum(100) ,' 190569292'
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print '---'
#t=time.time()
#print 'n_sum(200)', n_sum(200)
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print "TIME:",time.time()-t
#print '---'
#t=time.time()
#print 'n_sum(250)', n_sum(250)
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print "TIME:",time.time()-t
#print '---'
#t=time.time()
#print 'n_sum(300)', n_sum(300)
#print 'cache size:',len(cache.keys())
#print 'function calls:',count
#print "TIME:",time.time()-t
