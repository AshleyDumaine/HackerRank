s = raw_input().strip().lower()
letters = [False] * 26
for ch in s:
	if ch.isalpha():
		letters[ord(ch) - 97] = True
print('not pangram' if False in letters else 'pangram')
