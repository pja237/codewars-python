#!/usr/bin/python

import re

def run_length_encoding(stream):
    return map(lambda i: [len(i[0]),i[1]] , re.findall('((.)\\2*)',stream) )


print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb", run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")
print "hello world!", run_length_encoding("hello world!")
