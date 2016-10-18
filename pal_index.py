#!/bin/python

import sys


def isPalindrome(s):
    for i in xrange(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
 
def palindromeIndex(s):
    for idx in xrange((len(s)+1)//2):
        if s[idx] != s[len(s)-idx-1]:
            if isPalindrome(s[:idx]+s[idx+1:]):
                return idx
            else:
                return len(s)-idx-1
    return -1

t = int(raw_input().strip())

for a0 in xrange(t):
	s = raw_input().strip()
	print(palindromeIndex(s))
