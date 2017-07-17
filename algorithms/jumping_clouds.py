#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

i = 0
steps = 0
while i < len(c):
    if len(c) - i <= 3:
        break
    if c[i+2] == 0:
        i += 2
    else:
        i += 1
    steps += 1

print steps + 1
