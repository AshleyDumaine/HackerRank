'''from itertools import combinations
t = int(raw_input().strip())
for a0 in xrange(t):
	n = int(raw_input().strip())
	in_val = map(int, raw_input().strip().split(' '))
	ors = 0
	for i in in_val:
		ors |= i
	print(2**(len(in_val) - 1) * ors)'''
t = int(raw_input().strip())
for m in range(t):
    n = int(raw_input().strip())
    l = map(int,raw_input().split())
    ort=0
    for y in l:
        ort|= y
    print (ort*(2**(n-1)))%((10**9)+7)
