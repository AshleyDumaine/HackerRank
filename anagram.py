#!/bin/python

import sys

def makeMap(s):
	the_map = {}
	for ch in s:
        	if ch not in the_map:
			the_map[ch] = 1
        	else:
			the_map[ch] +=1      
    	return the_map 

def findDiff(s):
	if len(s) % 2 != 0:
		print(-1)
		return
	start2 = len(s) // 2
	s1 = s[:start2]
	s2 = s[start2:]
	map1 = makeMap(s1)
	map2 = makeMap(s2)
	diff = 0	
	for k in map2.keys():
		if k not in map1:
			diff += map2[k]
		else:
			diff += max(0, map2[k] - map1[k])
	print(diff)

t = int(raw_input().strip())
for a0 in xrange(t):
	s = raw_input().strip()
	findDiff(s)
	
