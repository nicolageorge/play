import sys
def min_jumps(inp):
	dp = [sys.maxint for i in range(len(inp)+1)]
	for i in range(len(inp)-1, -1, -1):
		print i 
		if inp[i] > len(inp) - i:
			dp[i] = 1
		else:
			print 'i', i, 'elem', inp[i]
			for j in range(i, i+inp[i]+1, 1):
				dp[i] = min(dp[i], dp[j]+1)
				# dp[i] = min()

	print inp
	print dp

inp = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
min_jumps(inp)