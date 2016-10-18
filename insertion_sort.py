#!/bin/python
def insertionSort(ar):   
	for j in range(1, len(ar)):
		e = ar[j]
		for i in range(j-1, -1, -1):
			if ar[i] > e:
				ar[i+1] = ar[i]
				if i == 0:
					ar[i] = e
        		else:
				ar[i+1] = e
				break
		print ' '.join(map(str, ar)) 
	return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
