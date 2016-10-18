#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
	n,c,m = map(int, raw_input().strip().split(' '))
	ch = n // c
	res = 0
	temp = ch
	while temp / m > 0:
		res += temp / m
		temp = (temp / m) + (temp % m)
	print(ch + res)
