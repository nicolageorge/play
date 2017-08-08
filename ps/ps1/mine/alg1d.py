def find_peak(lst):
    if len(lst) <= 0:
        return None

    mid = len(lst) / 2

    if lst[mid] <= lst[mid+1]:
        mid = mid+1
    elif lst[mid] <= lst[mid-1]:
        mid = mid-1
    else:
        return mid

    left = lst[:mid]
    right = lst[mid:]
