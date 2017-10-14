def longest_substring(inp):
	slow_pointer = 0
	max_str = 1
	for i in range(1, len(inp)):
		if inp[i] == inp[i-1]:
			slow_pointer = i
		max_str = max(max_str, i-slow_pointer)
	print max_str+1

def dp_longest_substring(inp):
	dp = [1 for i in range(len(inp)+1)]
	for i in range(1, len(inp)):
		if inp[i] != inp[i-1]:
			dp[i] = dp[i-1]+1
		else:
			dp[i] = 1
	print dp

def dp_non_rep(inp):
	dp = [1 for i in range(len(inp)+1)]
	seen = {}
	maxi = 0
	for i in range(1, len(inp)):
		if inp[i] not in seen:
			seen[inp[i]] = True
			maxi = max(maxi, len(seen))
			# print maxi
		else: 
			seen = {}
	print maxi


st = "asdfghaaasdfghjklpo"
longest_substring(st)
dp_longest_substring(st)
dp_non_rep(st)