n = int(raw_input())
n_arr = []
for i in xrange(n):
    n_arr.append(raw_input())
q = int(raw_input())
q_arr = []
for i in xrange(q):
    q_arr.append(raw_input())

for i in q_arr:
    print n_arr.count(i)
