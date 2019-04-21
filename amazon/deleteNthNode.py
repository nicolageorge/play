class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LL:
    def __init__(self, root=None):
        self.root = root
        self.last_node_added = root

    def add(self, node):
        if(self.root):
            self.last_node_added.next = node
            self.last_node_added = node
        else:
            self.root = node
            self.last_node_added = node

    def delete(self, nth):
        node = self.root
        counter = 0
        while(node):
            if(counter == nth-1):
                node.next = node.next.next
            counter += 1
            node = node.next


    def __str__(self):
        node = self.root
        vals = []
        while(node):
            vals.append(node.val)
            node = node.next
        return ', '.join([str(v) for v in vals])


def list_ops():
    l = LL()
    for i in range(100):
        n = Node(i)
        l.add(n)

    l.delete(17)
    l.delete(17)
    l.delete(17)
    l.delete(17)

    print(l)

if __name__ == '__main__':
    list_ops()
