#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())

cat = n / len(s)
rest = n % len(s)

repeats = cat * s.count('a') + s[:rest].count('a')
print repeats
