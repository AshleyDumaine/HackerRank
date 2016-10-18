def makeMap(s):
	the_map = {}
	for ch in s:
        	if ch not in the_map:
			the_map[ch] = 1
        	else:
			the_map[ch] +=1      
    	return the_map 

def isValidString(s):
	map = makeMap(s)
	lst = list(map.values())
	# print map
	# print map.values()
	wcount = 0
	wval = 0
	for count in map.values():
		if count != lst[0]:
			wcount += 1
			wval = count
			if wcount > 1 or (abs(wval - lst[0]) > 1 and (lst[0] != 1 and wval != 1)):
				print 'NO'
				return
	print 'YES'

s = raw_input().strip()
isValidString(s)
