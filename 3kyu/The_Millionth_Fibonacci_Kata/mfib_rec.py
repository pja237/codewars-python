#!usr/bin/python

import time

map=dict()
map[0]=0
map[1]=1

def mfib_rec_straight(n):
    if n==0:
        return 0
    elif n==1:
        return 1

    return mfib_rec_straight(n-1)+mfib_rec_straight(n-2)

def mfib_rec_top_down(n):
    if n==0:
        return map[0]
    elif n==1:
        return map[1]

    if not n in map.keys():
        map[n]=mfib_rec_top_down(n-1)+mfib_rec_top_down(n-2)

    return map[n]

def mfib_rec_bottom_up(n):
    mp=[0,1,1] 
    if 0<=n<=2: return mp[n]
    for i in xrange(n-2):
        mp=[mp[1],mp[2],mp[1]+mp[2]]
    return mp[-1]

def mfib_rec(n):
    res=0
    start_t=time.time()
    #res=0-mfib_rec_top_down(abs(n)) if n<0 and n%2==0 else mfib_rec_top_down(abs(n))
    #res=0-mfib_rec_straight(abs(n)) if n<0 and n%2==0 else mfib_rec_straight(abs(n))
    res=0-mfib_rec_bottom_up(abs(n)) if n<0 and n%2==0 else mfib_rec_bottom_up(abs(n))
    print n,"TIME:",time.time()-start_t,
    return res



#print "0:",mfib_rec(0)
#print "1:",mfib_rec(1)
#print "2:",mfib_rec(2)
#print "3:",mfib_rec(3)
#print "4:",mfib_rec(4)
#print "5:",mfib_rec(5)
#print "-5:",mfib_rec(-5)
#print "100:",mfib_rec(100)
#print "-100:",mfib_rec(-100)
#print "1k:",mfib_rec(1000)
# --- here is where recurtion exceeds max depth, even in mem-dp version of the recursive algorithm ---
#print "10k:",mfib_rec(10000)
#print "100k:",mfib_rec(100000)
#print "500k:",mfib_rec(500000)
#print "1m:"
mfib_rec(100000)
print
mfib_rec(500000)
print
mfib_rec(1000000)
print
#print "done"
