#!/usr/bin/python

def palindrome_chain_length(n):
    steps=0
    while not str(n)==str(n)[::-1]:
        print n
        steps+=1
        n+=int(str(n)[::-1])
    print n
    return steps

print palindrome_chain_length(787), 0
print palindrome_chain_length(87), 4
