import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    if n == 0:
        print 1
    else:
        height = 1
        for c in xrange(n):
            if c % 2 != 0:
                height += 1
            else:
                height *= 2
        print height
