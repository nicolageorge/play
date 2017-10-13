class Node(object):
    def __init__(self, results):
        self.results = results
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_front(self, node): pass
    def append_to_front(self, node): pass
    def remove_from_tail(self): pass

class Cache(object):
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.size = 0
        self.lookup = {}
        self.linked_list = LinkedList()

    def get(self, query):
        """ get stored query result from Cache
        accessing a node updates it's position to the front of LRU list"""
        node = self.lookup[query]
        if node is None:
            return None
        self.linked_list.move_to_front(node)
        return node.results

    def set(self, results, query):
        """set the result for the given query key in the cache
        when updating an entry update it's position in the front of LRU list
        if the entry is new and the cache is at capacity, remove oldest entry
        before new entry is added"""
        node = self.lookup[query]
        if node is not None:
            node.results = results
            self.linked_list.move_to_front(node)
        else:
            self.size += 1

        new_node = Node(results)
        self.linked_list.append_to_front(new_node)
        self.lookup[query] = new_node
