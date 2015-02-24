#!/usr/bin/python

import time

main={}
mainl=list()

def hamming(n):
    global main
    global mainl
    if n<len(mainl):
        return mainl[n-1]
    else:
        if n<10000: hamnum(10000)
        else: hamnum(n)
        return mainl[n-1]

def hamnum(n):
    global main
    global mainl
    s={1}
    main=set({1})
    
    while True:
       s2=set(map(lambda i: i*2, s)) 
       s3=set(map(lambda i: i*3, s)) 
       s5=set(map(lambda i: i*5, s)) 
       s={}
       s=set.union(s2,s3,s5)
       main=main.union(s)
       main=set(sorted(main)[:n])
       if min(s)>max(main): break
    mainl=sorted(main)

    return None

t=time.time()
print hamming(1)
print hamming(10)
print hamming(50)
print hamming(100)
print hamming(500)
print hamming(5000)
print hamming(10000)
print time.time()-t

