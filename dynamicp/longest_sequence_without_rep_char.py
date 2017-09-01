def longest_nonrep_seq(inp):
    i, j = 0, 0
    maxi = 1
    for i in range(1, len(inp)):
        if inp[i] == inp[i-1]:
            j = i+1
        maxi = max(maxi, i-j+1)
    print maxi


def dp_longest_nonrep_seq(inp):
    dp = [0 for i in range(len(inp))]
    dp[0] = 1
    maxi = 0
    for i in range(1, len(inp)):
        if inp[i] == inp[i-1]:
            dp[i] = 1
        else:
            dp[i] = 1 + dp[i-1]
        if dp[i] > maxi:
            maxi = dp[i]
    print maxi


st = 'abcaabcfffff'
dp_longest_nonrep_seq(st)
longest_nonrep_seq(st)
