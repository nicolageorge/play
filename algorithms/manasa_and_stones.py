import sys

def manasa_stones(a, b, stones):
    i = 0
    ret = []
    while i < stones:
        the_sum = (a * i) + (b * (stones-1-i))
        ret.append(the_sum)
        i += 1

    return ' '.join( map(str, sorted(set(ret))) )



tests = int(raw_input().strip())
out = []
for t in range(tests):
    stones = int(raw_input().strip())
    a = int(raw_input().strip())
    b = int(raw_input().strip())
    # print tests
    out.append( manasa_stones(a, b, stones) )

for i in out:
    print i
