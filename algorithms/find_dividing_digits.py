#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    cnt = 0
    for v in str(n):
        if v != '0' and n % int(v) == 0:
            cnt += 1
    print cnt
