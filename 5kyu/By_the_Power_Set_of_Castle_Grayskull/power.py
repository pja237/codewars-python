#!/usr/bin/python

ccalls=0
cache=dict()


# Doesn't work with floating points in array... floats "change" (get rounded) when being tossed into dictionary... 
def power_dp(S):
	global ccalls
	global cache
	ccalls+=1
	if not S:
		cache[str(S)]=[[]]
		return [[]]

	e=S[-1]

	if not str(S[:-1]) in cache.keys():
		cache[str(S[:-1])]=power_dp(S[:-1]) + [ i+[e] for i in power_dp(S[:-1]) ]

	return cache[str(S[:-1])]

def power_rec(S):
	global ccalls
	ccalls+=1
	if not S:
		return [[]]
	e=S[-1]
	return power_rec(S[:-1]) + [ i+[e] for i in power_rec(S[:-1]) ]

print power_rec([1,2,3])
print "func calls",ccalls
ccalls=0
print power_dp([1,2,3])
print "func calls",ccalls

print power_dp([0.04317037378772426, 0.07535647761428899, 0.10218731666146652, 0.17356312663567264])
