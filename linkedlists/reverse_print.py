"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    root = head
    output = [root.data]
    while root.next:
        root = root.next
        output.append(root.data)
    for e in output[::-1]:
        print e