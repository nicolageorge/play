inputs = int(raw_input().strip())
nums = map(int, raw_input().strip().split(' '))

maxim = 0
for n in nums:
    n_count = nums.count(n)
    n_minus_count = nums.count(n-1)
    if n_count + n_minus_count > maxim:
        maxim = n_count + n_minus_count
print maxim
