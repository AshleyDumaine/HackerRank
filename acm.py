#!/bin/python

import sys


n,m = map(int, raw_input().strip().split(' '))
topic = []
max_t = 0
teams = 0
for i in xrange(n):
	topic_t = int(str(raw_input().strip()), 2)
	topic.append(topic_t)
for i in xrange(n - 1):
	for j in range(i + 1, n):
		knowledge = topic[i] | topic[j]
		binary = bin(knowledge)[2:]
		tops = binary.count('1')
		if tops > max_t:
			max_t = tops
			teams = 1
		elif tops == max_t:
			teams += 1
print(max_t)
print(teams)
