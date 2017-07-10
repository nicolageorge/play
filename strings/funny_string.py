#!/bin/python

import sys

def funnyString(s):
	cmp = s[::-1]
	i = 0
	while i < len(s) - 1:
		if abs( ord(s[i]) - ord(s[i+1]) ) != abs( ord(cmp[i]) - ord(cmp[i+1]) ):
			return "Not Funny"
		i += 1
	return "Funny"

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)

