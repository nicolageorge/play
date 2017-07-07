[ints, rotatios] = map(int, raw_input().strip().split(' '))
n = map(int, raw_input().strip().split(' '))

def left_rotate(l, n):
    return l[n:] + l[:n]

l = left_rotate(n, rotatios)
# print l
print ' '.join([str(x) for x in l])
