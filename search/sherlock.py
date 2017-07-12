import sys

def sherlock_calculate():
	ar_count = int(raw_input().strip())
	ar = map(int, raw_input().strip().split(' '))
	
	left_index, right_index = 0, len(ar)-1
	left_sum, right_sum = ar[0], ar[-1]

	while ar[left_index] is not ar[right_index]:
		# print 'left_sum', left_sum
		# print 'right_sum', right_sum

		# print 'left_index', left_index
		# print 'right_index', right_index

		if left_sum < right_sum:
			left_index += 1
			left_sum += ar[left_index]

		elif left_sum > right_sum:
			right_index -= 1
			right_sum += ar[right_index]

		else:
			if ar[left_index+1] is ar[right_index-1]:
				return 'YES'
			else:
				right_index -= 1
				left_index += 1
				right_sum += ar[right_index]
				left_sum += ar[left_index]
	return 'NO'


inputs = int(raw_input().strip())

for i in range(inputs):
	print sherlock_calculate()



