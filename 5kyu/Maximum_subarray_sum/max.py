#!/usr/bin/python

def maxSequence(arr):
    # test if all pos
    if len(filter(lambda i: i<0, arr))==len(arr): return sum(arr)
    max=0
    for i in xrange(1,len(arr)+1):
        print arr
        for j in xrange(0,len(arr)-i+1):
            print arr[j:j+i]
            s=sum(arr[j:j+i])
            if s>max: max=s
    return max


print "---"
print maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print maxSequence([])
print maxSequence([-1,-2,-3,-4,-5])
print maxSequence([1,2,3,4])
print "---"
