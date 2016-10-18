#!/bin/python

import sys


n = int(raw_input().strip())
comps = []
for i in xrange(n):
	comp = set(list(str(raw_input().strip())))
	comps.append(comp)
u = set.intersection(*comps) 
print(len(u))
