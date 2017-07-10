def is_panagram(inp):
	alphabet = [chr(i) for i in range( ord('a'), ord('z')+1 )]
	inp2 = []
	for l in inp:
		inp2 += list(l)
	
	for c in sorted(alphabet):
		if c not in sorted(set(inp2)):
			return 'not pangram'
	return 'pangram'


inp = raw_input().strip().lower().split()
print is_panagram(inp)
