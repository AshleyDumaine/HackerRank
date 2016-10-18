#!/bin/python
def insertionSort(ar):
	count = 0
        for j in range(1, len(ar)):
                e = ar[j]
                for i in range(j-1, -1, -1):
                        if ar[i] > e:
                                ar[i+1] = ar[i]
				count += 1
                                if i == 0:
                                        ar[i] = e
                        else:
                                ar[i+1] = e
                                break
                # print ' '.join(map(str, ar))
		# print count
        print count
	return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
