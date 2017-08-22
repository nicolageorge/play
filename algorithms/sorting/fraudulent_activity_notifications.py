# 9 5
# 2 3 4 2 3 6 8 4 5
def bank_notifications(total_days, check_days, nums):
    notifications = 0
    for i in xrange(check_days, total_days+1):
        last_transactions = nums[i-check_days:i]
        sorted_last_transactions = sorted(last_5_transactions)
        

        if len(sorted_last_transactions)>=3 and nums[i-1] >= 2*sorted_last_transactions[2]:
            print sorted_last_transactions, nums[i-1], 2*sorted_last_transactions[2]
            notifications += 1
    return notifications

[total_days, check_days] = map(int, raw_input().strip().split(' '))
nums = map(int, raw_input().strip().split(' '))

print bank_notifications(total_days, check_days, nums)
