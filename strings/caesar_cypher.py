#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

ret = ''
for c in s:
	if c.isalpha():
		add = chr(ord(c)+k)
	else:
		add = c
	ret = '{}{}'.format(ret, add) 

print ret