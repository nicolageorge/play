[n, k] = map(int, raw_input().strip().split())
nums = map(int, raw_input().strip().split())

# count = 0
# for i in range(len(nums)):
# 	for j in range(i,len(nums),1):
# 		if abs( nums[i] - nums[j] ) == k:
# 			count += 1
# print count

nums = sorted(nums)
i, j, count = 0, 1, 0
while j < n:
	diff = nums[j] - nums[i]
	if diff == k:
		count += 1
		j += 1
	if diff < k:
		j += 1
	if diff > k:
		i += 1
print count