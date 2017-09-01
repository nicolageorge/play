# http://www.geeksforgeeks.org/longest-increasing-subsequence/
# Let us discuss Longest Increasing Subsequence (LIS) problem as an example
# problem that can be solved using Dynamic Programming.
# The Longest Increasing Subsequence (LIS) problem is to find the length of the
# longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
# longest-increasing-subsequence
#
# More Examples:
#
# Input  : arr[] = {3, 10, 2, 1, 20}
# Output : Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20
#
# Input  : arr[] = {3, 2}
# Output : Length of LIS = 1
# The longest increasing subsequences are {3} and {2}
#
# Input : arr[] = {50, 3, 10, 7, 40, 80}
# Output : Length of LIS = 4
# The longest increasing subsequence is {3, 7, 40, 80}

def long_adjacent_increase_subseq(arr):
    # dp[i] = dp[i-1] + (1 if seq[i] > seq[i-1] else 0)
    memory = [1 for x in range(len(arr))]
    maxi = 0
    for i in range(len(arr)):
        memory[i] = memory[i-1]
        if seq[i] > seq[i-1]:
            memory[i] += 1
        else:
            memory[i] = 1
        if memory[i] > maxi:
            maxi = memory[i]

    return memory


def longest_increasing_subseq(arr):
    dp = [1 for x in range(len(arr))]
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
    print dp



seq = [10, 22, 9, 33, 21, 50, 41, 60, 80]
longest_increasing_subseq(seq)
