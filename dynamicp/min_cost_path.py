rows = 3
cols = 3
def min_cost(cost, m, n):
	dp = [[0 for x in range(cols)] for y in range(rows)]
	dp[0][0] = cost[0][0]

	# init first row and col
	for i in range(1, m+1):
		dp[i][0] = dp[i-1][0] + cost[i][0]
	for i in range(1, n+1):
		dp[0][i] = dp[0][i-1] + cost[0][i]

	# construct rest of dp array
	for i in range(1, m+1):
		for j in range(1, n+1):
			dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + cost[i][j]

	print cost
	print dp

cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
min_cost(cost, 2, 2)
