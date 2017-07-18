agents = int(raw_input().strip())
call_number = int(raw_input().strip())
operators = []

def parse(start, end):
	global operators
	for i, (s, f,) in enumerate(operators):
		if start >= f:
			x[i] = [start, end]
			break
	else:
		operators.append([start, end])


for call in range(call_number):
	[call_start, call_end] = map(int, raw_input().strip().split(' '))
	parse(call_start, call_end)

print len(operators) - agents
