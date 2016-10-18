#!/bin/python
def makeMap(ar):
        the_map = {}
        for i in ar:
                if i not in the_map:
                        the_map[i] = 1
                else:
                        the_map[i] +=1
        return the_map

n = int(raw_input().strip())
ar = [int(i) for i in raw_input().strip().split(' ')]
map = makeMap(ar)
out = ""
for i in xrange(99):
	if i in map.keys():
		out += str(map[i]) + " "
	else:
		out += "0 "
if 99 in map.keys():
	out += str(map[99]) + " "
else:
	out += "0"
print out
