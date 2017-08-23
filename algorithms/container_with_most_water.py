a = [1, 2, 6, 5, 2, 3, 8, 2, 4]
maxArea = 0

left, right = 0, len(a)-1

while left < right:
    min_val = min(a[left], a[right])
    diff = right-left

    if maxArea < min_val * diff:
        maxArea = min_val * diff
        print 'maxArea', maxArea, 'left', left, 'right', right, 'min_val', min_val, 'diff', diff

    if a[left] < a[right]:
        left += 1
    else:
        right -= 1
    print left, right

print maxArea
