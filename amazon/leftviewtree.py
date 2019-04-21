class Tree:
    def __init__(self):
        self.last_printed_level = None

    def print_left_view(self, node=None, level=0):
        if(level == 0):
            print(node.val)
            self.last_printed_level = level
        elif(self.last_printed_level < level):
            print(node.val)
            self.last_printed_level = level

        if(node.left):
            self.print_left_view(node=node.left, level=level+1)
        if(node.right):
            self.print_left_view(node=node.right, level=level+1)


class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def main():
    root = Node(4)

    left1 = Node(2, parent=root)
    root.left = left1

    right1 = Node(6, parent=root)
    root.right = right1

    left21 = Node(1, parent=left1)
    left1.left = left21

    right21 = Node(3, parent=left1)
    left1.right = right21

    left22 = Node(5, parent=right1)
    right1.left = left22

    right22 = Node(7, parent=right1)
    right1.right = right22

    tree = Tree()
    tree.print_left_view(node=root)

if __name__ == '__main__':
    main()