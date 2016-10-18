n = int(raw_input().strip())
ar = map(int, raw_input().split())
ar.sort()
pair_list = []
curr_min_diff = float('inf')
for i in range(1, n):
	diff = abs(ar[i-1] - ar[i])
	if curr_min_diff > diff:
		curr_min_diff = diff
		del pair_list[:]
		pair_list.append((ar[i-1], ar[i]))
	elif curr_min_diff == diff:
		pair_list.append((ar[i-1], ar[i]))
for pair in pair_list:
	print("%d %d" % (pair[0], pair[1])),	
