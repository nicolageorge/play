#!/bin/python

import sys

def comp(lst):		
	n = int(raw_input().strip())
	lst = []
	for i in xrange(n):
	    t = str(raw_input().strip())

	    number_split_list = [list(x) for x in lst]
		for list_number in number_split_list:



	    lst.append(t)
	    
	assoc_sizes = [(len(x), x) for x in lst]
	sizes = [len(x) for x in lst]
	if len(set(sizes)) == len(sizes):
		for a in sorted(assoc_sizes, key=lambda (k, v): (k, v)):
			print a[1]
	else:
		

comp(lst)

