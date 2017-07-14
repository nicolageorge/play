import sys

[items_no, alergy_index] = map(int, raw_input().strip().split(' '))
items = map(int, raw_input().strip().split(' '))
anna_pay = int(raw_input().strip())

all_items_sum = sum(items)

if ( all_items_sum - items[alergy_index] ) / 2 == anna_pay:
    print "Bon Appetit"
else:
    print anna_pay - ( ( all_items_sum - items[alergy_index] ) / 2 )
