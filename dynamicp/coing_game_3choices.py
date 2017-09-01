# Coin game winner where every player has three choices
# A and B are playing a game. At the beginning there are n coins. Given two more numbers x
# and y. In each move a player can pick x or y or l coins. A always starts the game.
# The player who picks the last coin wins the game.
# For a given value of n,
# find whether A will win the game or not if both are playing optimally.
#
# Examples:
#
# Input :  n = 5, x = 3, y = 4
# Output : A
# There are 5 coins, every player can pick 1 or
# 3 or 4 coins on his/her turn.
# A can win by picking 3 coins in first chance.
# Now 2 coins will be left so B will pick one
# coin and now A can win by picking the last coin.
#
# Input : 2 3 4
# Output : B

# example values for x = 3, y=4
# n=0 A can't pick coins, he loses
# n = 1 A can pick 1 coin and win
# n = 2 A can pick 1 coin, B picks last coin, wins
# n = 3, 4 A will win by picking 3 or 4
# n = 5, 6 A will pick 3 or 4, b will have to pick between 2 coins, picks 1, A picks last

# OBS: A wins game for n coins when it loses for n-1, n-x and n-y
def find_winner(x, y, n):
    # store results
    dp = [0 for x in range(n+1)]

    # initial values
    dp[0] = False
    dp[1] = True

    for i in range(2, n+1):
        # if A loses any of i-1, i-x or i-y game, he will win game i
        if i-1 >= 0 and not dp[i-1]:
            dp[i] = True
        elif i-x >= 0 and not dp[i-x]:
            dp[i] = True
        elif i-x >= 0 and not dp[i-y]:
            dp[i] = True
        else:
            # A loses
            dp[i] = False

    return dp

print find_winner(2, 3, 4)
