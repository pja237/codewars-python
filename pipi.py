#!/usr/bin/python

import sys
import inspect

def pipi(a,b):
	print a,b
	f=inspect.currentframe()
	f=f.f_back
	print f.f_code
	print dir(f.f_code)
	print f.f_code.co_consts
	return

def tutu(x,y):
	pipi('pipi','tutu')
	pass

tutu('lala','lulu')
