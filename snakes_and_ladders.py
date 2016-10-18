from collections import deque

cases = int(raw_input().strip())
for i in range(cases):
	graph = [0] * 104
	mark = [False] * 104
	n_ladders = int(raw_input().strip())
	for j in range(n_ladders):
		ladder = map(int, raw_input().strip().split(' '))
		graph[ladder[0]] = ladder[1]
	n_snakes = int(raw_input().strip())
	for j in range(n_snakes):
		snake = map(int, raw_input().strip().split(' '))
		graph[snake[0]] = snake[1]
	q = deque()
	ans = float("inf")
	q.append((1,0));
	mark[1]=True;
	while q:
		p = q.popleft()
		if p[0] == 100:
			ans = p[1]
			break
		for i in range(1, 7):
			x = p[0] + i
			if x > 100:
				continue
			if not mark[x]:
				mark[x]=True
				if graph[x] != 0:
					x = graph[x]
					mark[x] = True
				q.append((x, p[1] + 1))
	print(-1 if (ans == float("inf")) else ans)
