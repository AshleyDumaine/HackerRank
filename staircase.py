#!/bin/python

import sys


n = int(raw_input().strip())
for i in range(n - 1, -1, -1):
    print(" " * i + "#" * (n - i))
