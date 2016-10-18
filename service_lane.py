#!/bin/python

import sys


n,t = map(int, raw_input().strip().split(' '))
width = map(int,raw_input().strip().split(' '))
for a0 in xrange(t):
	i,j = map(int, raw_input().strip().split(' '))
	if 1 in width[i:j+1]:
		print(1)
	elif 2 in width[i:j+1]:	
		print(2)
	else:
		print(3)
