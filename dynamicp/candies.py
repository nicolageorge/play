#!/bin/python

import sys

def candies(n, arr):
	candy = [1 for x in range(n)]
	i = 1
	while i < n:
		if arr[i] > arr[i-1]:
			candy[i] = candy[i-1] + 1
		# else:
		# 	if i == 1:
		# 		candy[i+1] = candy[i] + 1
		i += 1

	i -= 1
	while i >= 1:
		if arr[i-1] > arr[i] and candy[i-1] <= candy[i]:
			candy[i-1] = candy[i] + 1
		# print i, arr[i-1], arr[i], candy
		i -= 1
	return sum(candy)

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = []
    arr_i = 0
    for arr_i in xrange(n):
        arr_t = int(raw_input().strip())
        arr.append(arr_t)
    result = candies(n, arr)
    print result
