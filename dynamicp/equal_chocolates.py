# https://www.hackerrank.com/challenges/equal/forum
# Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and may have distributed the chocolates unequally. One of the program managers gets to know this and orders Christy to make sure everyone gets equal number of chocolates.
#
# But to make things difficult for the intern, she is ordered to equalize the number of chocolates for every colleague in the following manner,
#
# For every operation, she can choose one of her colleagues and can do one of the three things.
#
#     She can give one chocolate to every colleague other than chosen one.
#     She can give two chocolates to every colleague other than chosen one.
#     She can give five chocolates to every colleague other than chosen one.
#
# Calculate minimum number of such operations needed to ensure that every colleague has the same number of chocolates.
#
# Input Format
#
# First line contains an integer denoting the number of testcases. testcases follow.
# Each testcase has lines. First line of each testcase contains an integer denoting the number of colleagues. Second line contains N space separated integers denoting the current number of chocolates each colleague has.
#
# Constraints
# 1<=T<=100
# 1<=N <= 10000
#
# Number of initial chocolates each colleague has <
#
# Output Format
#
# lines, each containing the minimum number of operations needed to make sure all colleagues have the same number of chocolates.
#
# Sample Input
#
# 1
# 4
# 2 2 3 7
#
# Sample Output
#
# 2
#
# Explanation
#
# 1st operation: Christy increases all elements by 1 except 3rd one
# 2 2 3 7 -> 3 3 3 8
# 2nd operation: Christy increases all element by 5 except last one
# 3 3 3 8 -> 8 8 8 8

def min_ops(n, choco):


test_cases_no = int(raw_input().strip())
for t in range(test_cases_no):
    n = int(raw_input().strip())
    choco = map(int, raw_input().strip().split(' '))
    print min_ops(n, choco)
