def noCamelCaseWords(s):
	if s == '':
		return 0
	
	cont = 1
	for c in s:
		if c.isupper():
			cont += 1
	return cont

s = raw_input().strip()
print noCamelCaseWords(s)