def palDiff(s):
	diffSum = 0
    	for idx in xrange((len(s)+1)//2):
        	if s[idx] != s[len(s)-idx-1]:
			diffSum += abs(ord(s[idx]) - ord(s[len(s)-idx-1]))	
    	return diffSum

t = int(raw_input().strip())
for a0 in xrange(t):
	print palDiff(raw_input().strip())
