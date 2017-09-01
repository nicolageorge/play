#
# Find length of longest subsequence of one string which is substring of another string
#
# Given two string X and Y. The task is to find the length of longest subsequence of string X which is substring in sequence Y.
#
# Examples:
#
# Input : X = "ABCD",  Y = "BACDBDCD"
# Output : 3
# "ACD" is longest subsequence of X which
# is substring of Y.
#
# Input : X = "A",  Y = "A"
# Output : 1
# Method 1 (Brute Force):
# Use brute force to find all the subsequence of X and for each subsequence check whether it is substring of Y or not. If it is substring of Y, maintain a maximum length varible and compare length with it.
#
# Method 2: (Dynamic Programming):
# Let n be length of X and m be length of Y. Create a 2D array
#  dp[][] of m + 1 rows and n + 1 columns. Value dp[i][j] is maximum
# length of subsequence of X[0...j] which is substring of Y[0...i].
# Now for each cell of dp[][] fill value as :
#
# for (i = 1 to m)
#   for (j = 1 to n)
#     if (x[i-1] == y[j - 1])
#       dp[i][j] = dp[i-1][j-1] + 1;
#     else
#       dp[i][j] = dp[i][j-1];
#
# And finally, the length of the longest subsequence of x which is substring of y is max(dp[i][n]) where 1 <= i <= m.
import sys
# def max_seq_substring(x, y):
#     dp = [[0 for i in range(len(x)+1)] for j in range(len(y)+1)]
#
#     for i in range(len(y)+1):
#         for j in range(len(x)+1):
#             # if characters of string X an dY are equal, make dp[i][j] = 1 + dp[i-1][j-1]
#             if x[j-1] == y[i-1]:
#                 dp[i][j] = 1 + dp[i-1][j-1]
#             else:
#                 dp[i][j] = dp[i-1][j-1]
#
#     ret = 0
#     for i in range(len(y)):
#         if ret < dp[i][len(x)]:
#             ret = dp[i][len(x)]
#     return dp

#
# costs:
#     dp[i][j-1] = insert character
#     dp[i-1][j] = delete character
#     dp[i-1][j-1] = replace character


def longest_common_substring(A, B):
    dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]

    for i in range(len(A)+1):
        dp[i][0] = i

    for i in range(len(B)+1):
        dp[0][i] = i

    print dp

    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = 1 + min( dp[i+1][j], dp[i][j+1], dp[i][j] )
    print dp

    return dp[len(A)][len(B)]



def longest_common_substring2(first, second):
    dp = [[0 for i in range(len(second)+1)] for j in range(len(first)+1)]

    for i in range(len(first)+1):
        dp[i][0] = i

    for i in range(len(second)+1):
        dp[0][i] = i

    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = 1 + min(dp[i][j], dp[i+1][j], dp[i][j+1])
    # return dp
    print dp[len(first)][len(second)]

# longest_common_substring('asdfghjkl', 'qwertyuiop')
longest_common_substring2('asdfghjkl', 'qwertyuiop')



















































# print longest_common_substring('qwertyuiop', 'asdfghjkl')
