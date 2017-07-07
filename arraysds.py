#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print ' '.join([str(c) for c in arr[::-1]])
