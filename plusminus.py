#!/bin/python

import sys

n = float(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print("%.3f" % (sum(1 for num in arr if num > 0) / n))
print("%.3f" % (sum(1 for num in arr if num < 0) / n))
print("%.3f" % (sum(1 for num in arr if num == 0) / n))
