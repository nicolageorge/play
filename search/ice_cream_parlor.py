import sys

def calc_trips():
	money = int(raw_input().strip())
	flav_no = int(raw_input().strip())
	flavors = map(int, raw_input().strip().split(' '))
	for i, flav1 in enumerate(flavors):
		for j, flav2 in enumerate(flavors):
			if i != j and flav1 + flav2 == money:
				[small, big] = [i, j] if i < j else [j, i]
				return '{} {}'.format(small+1, big+1)
				

trips = int(raw_input().strip())

for trip in range(trips):
	print calc_trips()
