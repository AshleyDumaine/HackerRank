n,k = map(int, raw_input().split())
max = 0
ar = map(int, raw_input().split())
ar.sort()
curr_cost = 0
for elem in ar:
	if elem + curr_cost <= k:
		max += 1
		curr_cost += elem
	else:
		break
print max
