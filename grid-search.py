def isInGrid(R, G, r, g):
	for i in xrange(R):
		if i <= R - r and G[i].find(g[0]) != -1:
			indicies = []
			temp = i
			for j in xrange(r):
				indicies.append(G[temp].find(g[j]))
				temp += 1
			s = set(indicies)
			if len(s) == 1 and -1 not in s:
				print 'YES'
				return
	print 'NO'

t = int(raw_input().strip())
for a0 in xrange(t):
	R,C = map(int, raw_input().strip().split(' '))
	G = []
	for i in xrange(R):
		G.append(raw_input().strip())
	r,c = map(int, raw_input().strip().split(' '))
	g = []
	for i in xrange(r):
		g.append(raw_input().strip())
	isInGrid(R, G, r, g)		
