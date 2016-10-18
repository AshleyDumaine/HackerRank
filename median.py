n = int(raw_input().strip())
ar = map(int, raw_input().split())
ar.sort()
print ar[len(ar) // 2]
