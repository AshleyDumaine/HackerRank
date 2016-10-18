#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    	n = int(raw_input().strip())
	h = 1
	for y in xrange(n):
		h = h + 1 if y % 2 != 0 else h * 2
	print(h)
