#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())
nums = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine', 30: 'half'}
if m == 0:
	print('%s o\' clock' % nums.get(h))
elif m == 1:
	print('%s minute past %s' % (nums.get(m), nums.get(h)))
elif m == 15 or m == 30:
	print('%s past %s' % (nums.get(m), nums.get(h)))
elif m < 30:
	print('%s minutes past %s' % (nums.get(m), nums.get(h)))
elif 60 - m == 15:
	print('%s to %s' % (nums.get(60 - m), nums.get(h+1))if h < 12 else '%s minutes to %s' % (nums.get(60 - m), nums.get(1)))
elif 60 - m == 1:
	print('%s minute to %s' % (nums.get(60 - m), nums.get(h+1))if h < 12 else '%s minutes to %s' % (nums.get(60 - m), nums.get(1)))
else:	
	print('%s minutes to %s' % (nums.get(60 - m), nums.get(h+1)) if h < 12 else '%s minutes to %s' % (nums.get(60 - m), nums.get(1)))

