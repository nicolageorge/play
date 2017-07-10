"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""
def SortedInsert(head, data):
    if head is None:
        node = Node(data=data)
        return node
    node = head
    while head is not None:
        if node.data >= data:
            i = Node(data=data, prev_node=node.prev, next_node = node)
            node.prev = i
            if i.prev is None:
                return i
            else:
                i.prev.next = i
                return head
        if node.next is None:
            i = Node(data=data, prev_node = node, next_node = None)
            node.next = i
            break
        node = node.next
    return head
