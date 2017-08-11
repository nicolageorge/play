# def prepend_action(arr, i, j):
#     ret = arr[i:j]
#     ret.extend(arr[:i])
#     ret.extend(arr[j:])
#     return ret
#
# def append_action(arr, i, j):
#     ret = arr[:i]
#     ret.extend(arr[j:])
#     ret.extend(arr[i:j])
#     return ret

# https://www.hackerrank.com/challenges/array-and-simple-queries

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self, sequence):
        self.head = Node(data=sequence[0])
        current = self.head
        for item in sequence[1:]:
            current.next = Node(data = item)
            current = current.next

def print_ll(head):
    cur = head
    while cur:
        print cur.data,
        cur = cur.next

def prepend_action(head, i, j):
    cur = head
    for i in range(i-2):
        cur = cur.next

    item_before_new_head = cur
    # print cur.data, 'asd'
    new_head = cur.next

    for i in range(j-1):
        cur = cur.next

    old_next = cur.next
    cur.next = head
    item_before_new_head.next = old_next

    print_ll(new_head)

    return new_head


[n, m] = map(int, raw_input().strip().split(' '))
arr = map(int, raw_input().strip().split(' '))

ll = LinkedList(arr)
head = ll.head


for k in range(m):
    [tp, i, j] = map(int, raw_input().strip().split(' '))
    # i -= 1
    # j -= 1

    if tp == 1:
        head = prepend_action(head, i, j)
    if tp == 2:
        arr = append_action(arr, i, j)
    # print ' '.join([str(x) for x in arr])

# print abs(arr[0]-arr[n-1])
# print ' '.join([str(x) for x in arr])
