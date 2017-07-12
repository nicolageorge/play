import sys

n_count = int(raw_input().strip())
n_num = map(int, raw_input().strip().split(' '))

m_count = int(raw_input().strip())
m_num = map(int, raw_input().strip().split(' '))

# output = []
# n_index = 0
# for i, m in enumerate(m_num):
# 	if n_index <= n_count-1:
# 	 	if n_num[n_index] != m:
# 			output.append(m)
# 		else:
# 			n_index += 1	
# 	else:
# 		output.append(m)

# print ' '.join([str(x) for x in sorted(set(output))])

lst = [0 for n in range(10001)]
for n in n_num:
	lst[n] -= 1
for m in m_num:
	lst[m] += 1

out = []
for i, e in enumerate(lst):
	if e > 0:
		out.append(i)
print ' '.join( [str(i) for i in out] )