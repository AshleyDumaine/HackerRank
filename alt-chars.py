#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
	s = raw_input().strip()
	dels = 0
	for i in range(1, len(s)):
		if s[i] == s[i - 1]:
			dels += 1
	print(dels)	 
