#!/bin/python

import sys

def min_candy(v1, v2, c1, c2):
	min = min(c1, c2)
	if v1==v2:



	if arr[i] < arr[i-1]:
	candy[i] > candy[i+1]:

		candy[i] = 1

def candies(n, arr):
	candy = []
	# candy[0] = min(arr)
	candy = [0 for x in range(n)]
	baddest_kid = min(arr)
	# Complete this function
	i = 0
	while i < n-1:
		candy[i] = min_candy(arr[i], arr[i+1], candy[i], candy[i+1])
		# i += 1

	while i > 0:
		i -= 1
	return candy

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = []
    arr_i = 0
    for arr_i in xrange(n):
        arr_t = int(raw_input().strip())
        arr.append(arr_t)
    result = candies(n, arr)
    print result
