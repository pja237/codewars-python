#!/usr/bin/python

def nbr_of_laps(b, c):
	cc=1
	print "bob length:",b,"charles length",c
	while (c*cc)%b != 0: cc+=1
	print "total run length:",cc*c
	bc=(c*cc)/b
	print "bob circles",bc,"charles circles",cc
	return [bc,cc]

print nbr_of_laps(2,3)
print
print nbr_of_laps(3,2)
print
print nbr_of_laps(1,2)
print
print nbr_of_laps(2,1)
