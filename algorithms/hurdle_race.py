import sys

[n, k] = map(int, raw_input().strip().split(' '))
hurdles = map(int, raw_input().strip().split(' '))
max_hurdles = max(hurdles)

if k < max_hurdles:
    print max_hurdles - k
else:
    print 0
