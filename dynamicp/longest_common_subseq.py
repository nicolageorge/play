# Dynamic Programming | Set 4 (Longest Common Subsequence)
#
# We have discussed Overlapping Subproblems and Optimal Substructure properties in
# Set 1 and Set 2 respectively. We also discussed one example problem in Set 3.
# Let us discuss Longest Common Subsequence (LCS) problem as one more example
# problem that can be solved using Dynamic Programming.
#
# LCS Problem Statement: Given two sequences, find the length of longest
# subsequence present in both of them. A subsequence is a sequence that appears in
# the same relative order, but not necessarily contiguous.
# For example, "abc", "abg", "bdf", "aeg", "acefg", etc are subsequences
# of "abcdefg". So a string of length n has 2^n different possible subsequences.
#
# It is a classic computer science problem, the basis of diff (a file comparison
# program that outputs the differences between two files), and has applications
# in bioinformatics.
#
# Examples:
# LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
# LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.


# a = [[1, 2, 3, 10], [4, 5, 6, 20], [7, 8, 9, 30], [40, 50, 60, 70]]
# print a[1][3]
#
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         print a[i][j]
#     break


def longest_common_subseq(m_seq, n_seq):
    dp = [[0 for i in xrange(len(n_seq)+1)] for j in xrange(len(m_seq)+1)]
    if m_seq[0] == n_seq[0]:
        for i in range(len(m_seq)):
            dp[0][i] = 1
        for i in range(len(n_seq)):
            dp[i][0] = 1
    # print dp

    for i in range(1, len(m_seq)+1):
        for j in range(1, len(n_seq)+1):
            if m_seq[i-1] == n_seq[j-1]:
                # dp[i][j] = 1 + max( dp[i-1][j], dp[i][j-1] )
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                # print i, j
                dp[i][j] = max( dp[i-1][j], dp[i][j-1] )
                # print 'end', i, j
        # print j, i

    ret = [0 for x in range(dp[-1][-1])]
    index = dp[-1][-1]
    # start from right-bottom and store characters
    i, j = len(dp)-1, len(dp[0])-1
    while i > 0 and j > 0:
        # if current character in sequences are the same, then
        # it is part of the longest_common_subseq
        if m_seq[i-1] == n_seq[j-1]:
            ret[index-1] = m_seq[i-1]
            i -= 1
            j -= 1
            index -= 1
        # if not the same, find the larger of two and
        # go in the direction of the larger value
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    # print ret
    return ' '.join([str(x) for x in ret])


    # print dp
    # return dp


[m, n] = map(int, raw_input().strip().split(' '))
m_seq = map(int, raw_input().strip().split(' '))
n_seq = map(int, raw_input().strip().split(' '))
print longest_common_subseq(m_seq, n_seq)

# longest_common_subseq([1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3])
