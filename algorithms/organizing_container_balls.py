#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    M = []
    no_balls_in_container = [0 for x in xrange(n)]
    for M_i in xrange(n):
        M_temp = map(int,raw_input().strip().split(' '))
        M.append(M_temp)
        no_balls_in_container[M_i] = sum(M_temp)

    for i in xrange(n):
    	the_sum = 0
    	for j in xrange(n):
    		the_sum += M[j][i]	
    	for k, i in enumerate(no_balls_in_container):
    		if i == the_sum:
    			no_balls_in_container[k] = 0
    			break
    if sum(no_balls_in_container) == 0:
    	print "Possible"
    else:
    	print "Impossible"
