#!/bin/python
import sys

def isAlternate(s):
	if len(s) == 1:
		return True
	st = s
	# print st.replace(s[0], '').replace(s[1], '')
	if st.replace(s[0], '').replace(s[1], '') == '':
		for i, c in enumerate(s[:-1]):
			if c == s[i+1]:
				return False
		return True
	else:
		return False

def getStringFromAlternates(c1, c2, s):
	ret = ''
	for c in s:
		if c in [c1, c2]:
			ret = '{}{}'.format(ret, c)
	print ret
	return ret

n = raw_input().strip()
s = raw_input().strip()
i = 0
max = 0
while i < len(s)-1:
	if isAlternate(getStringFromAlternates(s[i], s[i+1], s)) and max < len(getStringFromAlternates(s[i], s[i+1], s)):
		max = len(getStringFromAlternates(s[i], s[i+1], s))
	i += 1

print max