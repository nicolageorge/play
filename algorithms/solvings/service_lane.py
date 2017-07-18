x = raw_input().split()
N = int(x[0])
T = int(x[1])
ans = []
width = raw_input().split()
size = [1, 2, 3]
for a in range(T):
    y = raw_input().split()
    i = int(y[0])
    j = int(y[1])
    minimum = width[i]
    for b in range(i,j+1):
        if width[b] < minimum:
            minimum = width[b]
    ans.append(minimum)
for i in ans:
    print i
