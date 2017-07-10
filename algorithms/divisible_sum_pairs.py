import sys

def disvisibleSumPairs(n, k, ar):
    sums = 0
    i = 0
    for n in ar:
        for x in ar[i+1:]:
            if ( n + x ) % k == 0:
                sums += 1
        i += 1
    return sums

n, k = raw_input().strip().split(' ')
n, k = int(n), int(k)
ar = map(int, raw_input().strip().split(' '))
print disvisibleSumPairs(n, k, ar)
