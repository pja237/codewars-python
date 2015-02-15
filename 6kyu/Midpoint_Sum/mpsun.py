#!/usr/bin/python

def midpoint_sum(ints):
    mp=filter(lambda i: sum(ints[:i])==sum(ints[i+1:]), xrange(1,len(ints)-1))
    return mp[0] if mp else None


print midpoint_sum([1,2,3,4,5]) 
print midpoint_sum([4,1,7,9,3,9]) ,'= 3, "[4,1,7,9,3,9] should return 3")'
print midpoint_sum([1,0,1]) ,'= 1, "[1,0,1] should equal 1")'
print midpoint_sum([9,0,1,2,3,4]) ,'= 2, "[9,0,1,2,3,4] should equal 2")'
print midpoint_sum([0,0,4,0]) ,'= 2, "[0,0,4,0] should equal 2")'
print midpoint_sum([-10,3,7,8,-6,-13,21]) ,'= 4, "[8,-6,-13,21] should equal 4")'
print midpoint_sum([1,1,1,1,-5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) ,'=  52, "Large valid sequence: [1,1,1,1,-5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] should equal 52")'
