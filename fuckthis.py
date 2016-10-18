ad,am,ay = map(int, raw_input().strip().split(' '))
ed,em,ey = map(int, raw_input().strip().split(' '))
if ay < ey or (ay == ey and am < em) or (ay == ey and am == em and ad < ed):
	print 0
elif am == em and ay == ey:
	print 15 * (ad - ed)
elif ay == ey:
	print 500 * (am - em)
else:
	print 10000
