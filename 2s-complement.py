def twos_comp(val, bits):
	bits = 32
    	if val != 0:
		if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        		val = val - (1 << bits)        # compute negative value
    	return val 

t = int(raw_input().strip())
for a0 in xrange(t):
	a, b = map(int, raw_input().strip().split(' '))
	sum = 0
	for i in range(a, b + 1):
		bin_a = bin(twos_comp(i, i.bit_length()))[2:]
		sum += bin_a.count('1')
	print sum
