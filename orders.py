import operator

n = int(raw_input().strip())
orders = {}
for cust in range(1, n+1):
	t,d = map(int, raw_input().strip().split(' '))
	orders[cust] = t + d
sorted_orders = sorted(orders.items(), key=operator.itemgetter(1))
for elem in sorted_orders:
	print elem[0],
