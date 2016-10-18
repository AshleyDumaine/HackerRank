#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
while len(arr) > 0:
	print len(arr) 
	m = min(arr)
	arr[:] = [x - m for x in arr if x - m > 0]
