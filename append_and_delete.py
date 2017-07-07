#!/bin/python

import sys


# s = raw_input().strip()
# t = raw_input().strip()
# k = int(raw_input().strip())

def first_dif_letter(s, t, k):
	if len(s) > len(t):
		bigger, smaller = s, t
	else:
		bigger, smaller = t, s

	count = 0
	while bigger != smaller:
		if len(bigger) <> len(smaller):
			bigger = bigger[:-1]
			count += 1
		else:
			bigger = bigger[:-1]
			smaller = smaller[:-1]
			count += 2
		print bigger, smaller, count
	if k >= count:
		return 'Yes'
	else:
		return 'No'


s = 'zzzzz'
t = 'zzzzzzz'
k = 4
print first_dif_letter(s, t, k), 'True'

s = 'hackerhappy'
t = 'hackerrank'
k = 9
print first_dif_letter(s, t, k), 'True'


s = 'y'
t = 'yu'
k = 2
print first_dif_letter(s, t, k), 'True'

s = 'abcd'
t = 'abcdert'
k = 10
print first_dif_letter(s, t, k), 'True'
