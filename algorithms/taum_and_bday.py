import sys

tests = int(raw_input().strip())
for t in xrange(tests):
    [black_quantity, white_quantity] = map(int, raw_input().strip().split(' '))
    [black_cost, white_cost, conversion_cost] = map(int, raw_input().strip().split(' '))

    if black_cost < white_cost:
        [lower_cost, higher_cost, lower_quantity, higher_quantity] = [black_cost, white_cost, black_quantity, white_quantity]
    else:
        [lower_cost, higher_cost, lower_quantity, higher_quantity] = [white_cost, black_cost, white_quantity, black_quantity]

    if higher_cost - lower_cost > conversion_cost:
        # should_convert = True
        print ( lower_cost * lower_quantity ) + ( ( lower_cost + conversion_cost ) * higher_quantity )
    else:
        print ( lower_cost * lower_quantity ) + ( higher_cost * higher_quantity )
