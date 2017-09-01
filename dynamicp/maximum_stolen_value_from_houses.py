# http://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
# Find maximum possible stolen value from houses
#
# There are n houses build in a line, each of which contains some value in it.
# A thief is going to steal the maximal value of these houses, but he can't steal
# in two adjacent houses because owner of the stolen houses will tell his two neighbour
# left and right side. What is the maximum stolen value.
# Examples:
#
# Input  : hval[] = {6, 7, 1, 3, 8, 2, 4}
# Output : 19
# Thief will steal 6, 1, 8 and 4 from house.
#
# Input  : hval[] = {5, 3, 4, 11, 2}
# Output : 16
# Thief will steal 5 and 11

def maximum_stolen(seq):
    if len(seq) == 0:
        return 0
    if len(seq) == 1:
        return seq[0]
    if len(seq) == 2:
        return max(seq[0], seq[1])

    # dp[i] represents maximum value stolen so far after reaching house i
    dp = [0 for i in range(len(seq))]

    # init dp[0] and dp[1]
    dp[0] = seq[0]
    dp[1] = max(seq[0], seq[1])

    # fill remaining positions
    for i in range(2, len(seq)):
        # print i
        dp[i] = max(seq[i]+dp[i-2], dp[i-1])

    print dp[-1]

seq = [6, 7, 1, 3, 8, 2, 4]
maximum_stolen(seq)
