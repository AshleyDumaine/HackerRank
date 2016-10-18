#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
	n = int(raw_input().strip())
	tmp = n
	res = 0
	while tmp > 0:
		digit = tmp % 10
		tmp /= 10
		if digit != 0 and n % digit == 0:
			res += 1
	print(res)
