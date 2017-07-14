inputs = int(raw_input().strip())

for i in range(inputs):
    [cat_a, cat_b, mouse] = map(int, raw_input().strip().split(' '))
    if abs(cat_a - mouse) < abs(cat_b - mouse):
        print 'Cat A'
    elif abs(cat_a - mouse) > abs(cat_b - mouse):
        print 'Cat B'
    else:
        print 'Mouse C'
