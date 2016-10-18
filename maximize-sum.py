def largest_less_than(numlist, n):
	answer = min(numlist, key=lambda x: n-x if n>=x else float('inf'))
	if answer > n:
		answer = None
	return answer

t = raw_input().strip()
for a0 in xrange(t):
	sum = 0
	ans = 0
	n, m = map(int, raw_input().strip())
	ar = map(int, raw_input().strip().split(' '))
	s = []
	for i in xrange(n):
		sum += ar[i]
		sum %= m
		
