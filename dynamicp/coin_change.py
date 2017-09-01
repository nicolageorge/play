def cnt(arr, n):
    # we need n+1 rows, base case 0, n=0
    table = [[0 for x in range(len(arr))] for x in range(n+1)]

    # entrries for n = 0
    for i in range(len(arr)):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(len(arr)):
            # solutions including arr[j]
            x = table[ i-arr[j] ][j] if i - arr[j] >= 0 else 0

            # solutions excluding arr[j]
            y = table[i][j-1] if j >= 1 else 0

            table[i][j] = x + y
            print table

    return table[n][m-1]



arr = [1, 2, 3]
m = len(arr)
n = 4
print cnt(arr, n)
