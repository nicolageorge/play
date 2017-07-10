import sys

def super_reduced_string(s):
	i = 0
	while i < len(s)-1:
		if s[i] == s[i+1]:
			s = s[:i] + s[i+2:]
			i = 0
		else:
			i += 1
	if s == '':
		return "Empty String"
	else:
		return s


s = raw_input().strip()
print super_reduced_string(s)