import sys

def array_rotate(a, n):
    return  a[-n:] + a[:-n]

def arr_rotate(a, n):
    return a[n-]

n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
out = []
for a0 in xrange(q):
    m = int(raw_input().strip())
    rotated = array_rotate(a, k)
    out.append(rotated[m])

for o in out:
    print o
