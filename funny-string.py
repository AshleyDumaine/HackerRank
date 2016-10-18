#!/bin/python

import sys


def isFunny(s, r):
	for i in range(1, len(s)):
		if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i - 1])):
			print('Not Funny')
			return
	print('Funny')

t = int(raw_input().strip())
for a0 in xrange(t):
	s = raw_input().strip()
	r = s[::-1]
	isFunny(s, r)
