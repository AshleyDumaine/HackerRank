num = int(raw_input().strip())
size = int(raw_input().strip())
ar = [int(i) for i in raw_input().strip().split(' ')]
for i in range(size):
	if ar[i] == num:
		print i
