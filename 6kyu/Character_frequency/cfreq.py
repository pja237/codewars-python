#!/usr/bin/python

import string

def letter_frequency(text):
	return sorted(map(lambda i: (i,text.count(i)) , sorted(set(text.lower()) & set(string.lowercase))), key=lambda i: i[1], reverse=True)

print letter_frequency('wklv lv d vhfuhw phvvdjh')
