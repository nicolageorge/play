This must be an easy problem actually. all you have to do is sort the array, and then check the difference of adjacent pairs, if its less than ur last min value, update it only if the index of those pairs are in same way in original array.

n =  int(input().strip())
numbers = list(map(int,input().strip().split()))

nums = list(numbers)
nums.sort()
minCost = 10**10
for i in range(1,n):
    if (nums[i]-nums[i-1] < minCost)  and (numbers.index(nums[i]) < numbers.index(nums[i-1])):
        minCost = nums[i]-nums[i-1]
print(minCost)
