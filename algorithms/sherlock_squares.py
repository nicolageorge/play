def is_square(apositiveint, bigger_seen):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False, bigger_seen
        seen.add(x)
    bigger_seen += seen
    return True, bigger_seen

t = int(raw_input().strip())
big_seen = []
for i in range(t):
    count = 0
    [a, b] = map(int, raw_input().strip().split(' '))
    for i in range(a, b+1):
        if i > 0:
            tf, big_seen = is_square(i, big_seen)
            if tf:
                count += 1
    print count
