def isearch(arr, target):
    low, mid, high = 0, -1, len(arr)-1

    # while arr[mid] != target:
    i = 0
    while high > low:
        i += 1
        mid = low + int( (float(high-low)/(arr[high]-arr[low])) * (target-arr[low]) )
        # print arr[mid]
        if arr[mid] == target:
            return 'element at {} position'.format(mid)
        elif arr[mid] < target:
            low = mid+1
        elif arr[mid] > target:
            high = mid-1

    return 'Element not found, {} iteration'.format(i)



def pro(el):
    return (x+2*x)**2

arr = [pro(x) for x in range(2, 1260300)]
print isearch(arr, 743044)





# mod = low + (high-low)/(ar[high]-ar[low]) * target-ar[low]
