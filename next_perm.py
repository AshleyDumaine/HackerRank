def next_perm(w):
	i = len(w) - 2
	while not (i < 0 or w[i] < w[i+1]):
		i -= 1
	if i < 0:
		print 'no answer'
		return
	j = len(w) - 1
	while not (w[j] > w[i]):
		j -= 1
	str = list(w)
	str[i], str[j] = str[j], str[i]
	str[i+1:] = reversed(str[i+1:])
	print(''.join(str))

t = int(raw_input().strip())
for a0 in xrange(t):
	next_perm(raw_input().strip())
	
