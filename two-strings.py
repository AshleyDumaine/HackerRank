#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
	# a substring can be a single letter
	s1 = raw_input().strip()
	s2 = raw_input().strip()
	print 'YES' if set(list(s1)) & set(list(s2)) else 'NO'
	
