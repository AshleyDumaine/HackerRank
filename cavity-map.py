#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
for i in xrange(n):
	grid_t = str(raw_input().strip())
	grid.append(grid_t)
for i in range(1, n - 1):
	for j in range(1, n - 1):
		d = grid[i][j]
		if grid[i - 1][j] < d and grid[i + 1][j] < d and grid[i][j - 1] < d and grid[i][j + 1] < d:
			list1 = list(grid[i])
			list1[j] = 'X'
			grid[i] = ''.join(list1)
for i in range(n):
	print(grid[i])
