def sum_and_compare(ar1, ar2):
	for z in xrange(n):
		if ar1[z] + ar2[z] < k:
			print 'NO'
			return
	print 'YES'

t = int(raw_input().strip())
for a0 in xrange(t):
	n,k = map(int, raw_input().strip().split(' '))
	ar1 = map(int, raw_input().strip().split(' '))
	ar2 = map(int, raw_input().strip().split(' '))
	ar1.sort()
	ar2.sort(reverse=True)
	sum_and_compare(ar1, ar2)	
