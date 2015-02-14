#!usr/bin/python

def mfib(n):
    mp=[0,1,1] if n>0 else [0,-1,-1]
    if 0<=n<=2 or -2<=n<=0: return mp[n]
    for i in xrange(abs(n)-2):
        mp=[mp[1],mp[2],mp[1]+mp[2]]
    return mp[-1]


print "0:",mfib(0)
print "1:",mfib(1)
print "2:",mfib(2)
print "3:",mfib(3)
print "4:",mfib(4)
print "5:",mfib(5)
print "-5:",mfib(-5)
print "100:",mfib(100)
print "-100:",mfib(-100)
#print "1k:",mfib(1000)
#print "10k:",mfib(10000)
#print "100k:",mfib(100000)
#print "500k:",mfib(500000)
print "1m:"
mfib(1000000)
print "done"
