#!/usr/bin/python


def isvamp(a,b):
    c=list(str(a*b))
    notvamp=0
    print c
    for i in (a,b):
        for j in str(i):
            try:
                print "remove:",j
                c.remove(j)
            except:
                notvamp=1
                break
    print a,b,c
    if c or notvamp:
        return False
    else:
        return True

a=6
b=21
print isvamp(a,b)

a=10
b=11
print isvamp(a,b)
