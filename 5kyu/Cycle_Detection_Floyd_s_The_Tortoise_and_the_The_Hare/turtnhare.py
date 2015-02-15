#!/usr/bin/python

def floyd(f, x0):
    t=x0
    h=f(x0)
    while t!=h:
        t=f(t)
        h=f(f(h))
    print "V @",t,h
    # we're @ v-point, now we find mu
    t=x0
    h=f(h)
    mu=0
    while t!=h:
        print t, h
        mu+=1
        t=f(t)
        h=f(h)
    print t, h, mu
    # we found the start of the cycle, now just make 1 full circle and count 
    lam=1
    while f(t)!=h:
        t=f(t)
        lam+=1

    return [mu, lam]

def h(x):
    return (x+1)%175
    #return (x+1)%35
    #return (x+1)%5

print floyd(h,0)," [0,175]"
