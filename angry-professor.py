#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
	n,k = map(int,raw_input().strip().split(' '))
	arr = map(int,raw_input().strip().split(' '))
	print('YES' if sum(1 for a in arr if a <= 0) < k else 'NO')
