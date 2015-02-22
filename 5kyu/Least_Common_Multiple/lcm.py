#!/usr/bin/python

def lcm(*args):
    n=max(args)
    if filter(lambda i: i==0, args): return 0
    m=1
    while True:
        if filter(lambda i: (n*m)%i!=0 , args):
            m+=1
        else:
            break
    return n*m



print lcm(2,5),10
print lcm(2,3,4),12
print lcm(9),9
print lcm(0),0
print lcm(0,1),0
