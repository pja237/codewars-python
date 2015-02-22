#!/usr/bin/python

def hamming(a,b):
    return len(filter(lambda i: i[0]!=i[1], map(lambda i,j: (i,j), a,b)))

print hamming("I like turtles","I like turkeys")  ,'/returns 3'
print hamming("Hello World","Hello World")  ,'/returns 0'
