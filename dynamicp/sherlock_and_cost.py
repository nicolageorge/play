def max_dif(nums):
	# dp = [[0 for x in range(len(nums)+1)] for y in range(len(nums)+1)]
	dp = [0 for x in range(len(nums)+1)]
	arr = [0 for x in range(len(nums))]
	# for k in range(1, len(nums)):
	# 	max_sum = 0
	# 	for i in range(nums[k-1]):
	# 		for j in range(nums[k]):
	# 			# dp[i][j]
	# 			max_sum = max(max_sum, abs(j-i))
	# 	dp[k] = max_sum

	arr[0] = nums[0]
	for i in range(1, len(nums)):
		the_sum = 0
		for j in range(1, nums[i]):
			if abs(j-arr[i]) > the_sum:
				arr[i] = the_sum

	print nums
	print arr
	return the_sum
	# return sum(dp)


rets = [1121, 642, 508, 1107, 5563, 5012, 4858, 4256, 3585, 1228, 2849, 1709, 4550, 2603, 0, 3264, 3949, 0, 3242, 1888]

rets_cont = 0
test_cases = int(raw_input().strip())
for i in range(test_cases):
	n = int(raw_input().strip())
	nums = map(int, raw_input().strip().split())
	print max_dif(nums)
	print rets[rets_cont]
	rets_cont += 1
	break

