#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
	b,w = map(int, raw_input().strip().split(' '))
	x,y,z = map(int, raw_input().strip().split(' '))
	if (y + z) < x:
		# buy all w and convert b of them
		print(w * y + b * (y + z))
	elif (x + z) < y:
		# buy all b and convert w of them
		print(b * x + w * (x + z))
	else:
		print(b * x + w * y)
		
