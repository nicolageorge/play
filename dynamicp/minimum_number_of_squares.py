import sys
# if n <= 3, return n
# else:
#     minSquares(n) = min{ 1 + minSquares(n - x*x) } where x >= 1 and x*x <= n
#
# def minSquares(n):
#     # base cases
#     if n <= 3:
#         return n
#
#     res = n # max number of squares required is (1*1 + 1*1 + 1*1)
#
#     # go through all smaller numbers to recursivly find minimum
#     for x in range(n):
#         temp = x*x
#         print temp, n
#         if temp > n:
#             break
#         else:
#             res = min(res, 1+ minSquares(n - temp))
#     return res
#
#
# def dp_min_squares(n):
#     # dp memory table to store squares
#     dp = [sys.maxint for x in range(n+1)]
#
#     # base case
#     dp[0] = 0
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 3
#
#     for i in range(4, n+1):
#         #  max value can always be 1*1 + 1*1 + 1*1
#         dp[i] = i
#
#         # go through all smaller numbers to rec find minimum
#         for x in range(i):
#             temp = x*x
#             if temp > i:
#                 break
#             else:
#                 dp[i] = min(dp[i], 1+dp[i-temp])
#
#     # res = dp[n]
#     # del dp
#     # return res
#     return dp
# print dp_min_squares(20)




def dp_min_sq(n):
    dp = [sys.maxint for x in range(n+1)]
    dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
    for i in range(4, n+1):
        dp[i] = i
        for x in range(i):
            tmp = x*x
            if tmp>i:
                break
            else:
                dp[i] = min(dp[i], 1+dp[i-tmp])
    print dp

dp_min_sq(20)
