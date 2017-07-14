[money, keyboards_no, mouse_no] = map(int, raw_input().strip().split(' '))
keyboards = map(int, raw_input().strip().split(' '))
mouses = map(int, raw_input().strip().split(' '))

if min(keyboards) + min(mouses) > money:
    print -1
else:
    print max([sum([x, y]) for x in keyboards for y in mouses if sum([x, y]) <= money])
