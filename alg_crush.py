[n, m] = map(int, raw_input().strip().split(' '))
max = 0
x = 0
abk_list = []
aux = [0 for i in xrange(n+1)]
n_list = [0 for i in xrange(n)]
for i in xrange(m):
    [a, b, k] = map(int, raw_input().strip().split(' '))
    aux[a] += k
    if b + 1 <= n:
        aux[b+1] -= k
    print aux

for i in xrange(n+1):
    x = x + aux[i]
    if max < x:
        max = x

print max


# for i in range(m):
