import sys
def min_squares(num):
    dp = [i for i in range(num+1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for n in range(4, num+1):
        i = 1
        while i * i <= n:
            dp[n] = min( dp[n], 1 + dp[n-i*i] )
            i += 1

    return dp[num]

# num = int(raw_input().strip())
num = 54984
print min_squares(num)
