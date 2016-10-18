#!/bin/python

import sys

def decentNum(n):
	ftmp = n
	while ftmp % 3 != 0 and ftmp >= 3:
		ftmp -= 5
	if ftmp % 3 != 0:
		print('-1')
		return
	print('5' * ftmp + '3' * (n - ftmp))	

t = int(raw_input().strip())
for a0 in xrange(t):
	n = int(raw_input().strip())
	decentNum(n)	

