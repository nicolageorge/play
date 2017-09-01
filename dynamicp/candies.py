#!/bin/python

import sys

def min_candy(i, arr, candy):
	if i == 0:
		neighbor_value = arr[i+1]
		neighbor_c = candy[i+1]
	elif i == len(arr):
		neighbor_value = arr[i-1]
		neighbor_candy = candy[i-1]
	else:
		neighbor_value = max(arr[i-1], arr[i+1])
		neighbor_candy = max(candy[i-1], candy[i+1])

	if arr[i] > neighbor_value and candy[i] <= neighbor_candy:
		return neighbor_candy+1


def candies(n, arr):
	candy = []
	# candy[0] = min(arr)
	candy = [0 for x in range(n)]
	baddest_kid = min(arr)
	# Complete this function
	i = 0
	while i < n-2:
		if arr[i] > arr[i-1]:
			candy[i] = candy[i-1] + 1

	while i > 0:
		if arr[i] > arr[i+1]:
			candy[i] = candy[i-1] + 1

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
