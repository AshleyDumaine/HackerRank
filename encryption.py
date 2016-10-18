#!/bin/python

import sys
from math import sqrt
from math import ceil
from math import floor

s = raw_input().strip().replace(" ", "")
l = len(s)
sl = sqrt(l)
cols = int(ceil(sl))
rows = int(floor(sl))
if rows * cols < l:
	rows += 1
word = ""
for i in xrange(cols):
	for j in xrange(rows):
		if cols * j + i < l:	
			word += s[cols * j + i]
	word += " "
print(word)
