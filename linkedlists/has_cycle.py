"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head is None:
    	return None
    tortoise = head
    rabbit = head
    while tortoise is not None and tortoise.next is not None:
    	tortoise = tortoise.next
    	rabbit = rabbit.next.next
    	if tortoise is None or rabbit is None:
    		return 0
    	if rabbit == tortoise:
    		return 1
    return 0