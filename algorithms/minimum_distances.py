portocale = int(raw_input().strip())
nums = map(int, raw_input().strip().split(' '))

indices = {}
for n in set(nums):
	indices[n] = [i for i, x in enumerate(nums) if x == n]
# res = []

mini = 99999
for i in indices:
	res = [ abs(indices[i][k] - indices[i][k+1]) for k, x in enumerate(indices[i]) if k+1<len(indices[i]) ]
	if len(res):
		minimum_distance = min(res)
		if mini > minimum_distance:
			mini = minimum_distance

if mini == 99999:
	print -1
else:
	print mini

# print indices

# # abc -> bca -> cab
# 1 2 3 4 5
# 1 2 4 5 3
# 1 2 5 3 4
# 1 2 3 4 5


# 1 2 3 5 4
# 1 2 5 4 3
# 1 2 4 3 5
# 1 2 3 5 4

