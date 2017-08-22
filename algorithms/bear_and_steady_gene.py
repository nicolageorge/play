from collections import Counter
nums = int(raw_input().strip())
mean = nums / 4

sequence = raw_input().strip()

cnt = Counter(sequence)
# print cnt, mean

adds, subs = 0, 0

for c in ['A', 'G', 'T', 'C']:
    if c in cnt:
        if cnt[c] < mean:
            adds += mean - cnt[c]
        else:
            subs += cnt[c] - mean
    else:
        adds += mean

print cnt
print 'adds', adds
print 'subs', subs
# print (adds + subs) / 2
# print difference
