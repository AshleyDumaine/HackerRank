def findMaxSum(n,ar):
	curr_max = -2**31
	max_here = -2**31
	max_neg = -2**31
	c_sum = 0
	for i in xrange(n):
		max_here = max(ar[i], max_here + ar[i])
		curr_max = max(curr_max, max_here)
		if ar[i] > 0:
			c_sum += ar[i]
		else:
			if ar[i] > max_neg:
				max_neg = ar[i]
	if c_sum == 0:
		c_sum = max_neg
	print "%i %i" % (curr_max, c_sum)

t = int(raw_input().strip())
for a0 in xrange(t):
	n = int(raw_input().strip())
	ar = map(int, raw_input().strip().split(' '))
	findMaxSum(n,ar)


'''def dp(L):
    max_so_far = max_ending_here = -2**31
    c_sum = 0
    max_neg = -2**31

    for i in xrange(len(L)):
        max_ending_here = max(L[i], max_ending_here + L[i])        
        max_so_far = max(max_so_far, max_ending_here)

        if L[i] > 0:
            c_sum += L[i] 
        else:
            if L[i] > max_neg:
                max_neg = L[i]
    if c_sum == 0: # All values were negative so just pick the largest
        c_sum = max_neg
    return map(str, (max_so_far, c_sum))

if __name__ == '__main__':
    test_cases = int(raw_input())
    for i in xrange(test_cases):
        arr_length = int(raw_input())
        array = [int(i) for i in raw_input().split()]

        print ' '.join(dp(array))'''
