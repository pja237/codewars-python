#!/usr/bin/python

def divs(n):
    d=filter(lambda i: n%i==0, xrange(2,n/2+1))
    if d: return d
    else: return str(n)+" is prime"

print divs(15)
print divs(13)
