import sys

n = int(raw_input().strip())

def check_elem(matr, i, j):
    global n
    if i+1 > n-1 or i-1 < 0 or j+1 > n-1 or j-1 < 0:
        return matr[i][j]

    # print i, j, n
    max_close = max( [matr[i][j+1], matr[i][j-1], matr[i+1][j], matr[i-1][j]] )

    if matr[i][j] > max_close:
        return 'X'
    else:
        return matr[i][j]



matr = []
for x in range(n):
    nums = map(int, list(raw_input().strip()))
    matr.append(nums)

for i in range(n):
    for j in range(n):
        matr[i][j] = check_elem(matr, i, j)


for x in range(n):
    print ''.join([str(x) for x in matr[x]])
