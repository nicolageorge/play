[n, k] = map(int, raw_input().strip().split(' '))
clouds = map(int, raw_input().strip().split(' '))
energy = 100

for i in range(0, len(clouds), k):
    if clouds[i] == 1:
        energy -= 2
    energy -= 1

print energy
