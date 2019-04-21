class Node:
    def __init__(self, value, neighbors=None):
        self.value = int(value)
        if(isinstance(neighbors, list)):
            self.neighbors = neighbors
        elif(isinstance(neighbors, string)):
            self.neighbors = neighbors.split(',')

    def add_neighbor(self, node):
        self.neighbors.append(node)


class UndirectedGraph:
    def __init__(self):
        self.nodes = []
        self.adj_list = {}

    def add(self, node):
        self.nodes.append(node)
        self.adj_list[node.value] = node.neighbors

    def __str__(self):
        return ', '.join([n.value for n in self.nodes])

    def BFS(self, start):
        level = {start:0}
        parent = {start:None}
        i = 1 
        frontier = [start] # level i-1
        print('start: {}'.format(start))
        while frontier:
            nxt = [] # level i
            for f in frontier:
                # print('f:{}'.format(f))
                for v in self.adj_list[f]:
                    if v not in level:
                        level[v] = i
                        parent[f] = f
                        nxt.append(v)
                        print('v: {}'.format(v))
                frontier = nxt
                i += 1


if __name__ == '__main__':
    inp = input()
    args = inp.split('#')
    graph = UndirectedGraph()
    for n in args:
        nod = n.split(',')
        val = int(nod[0])
        neighbors = [int(n) for n in nod[1:]]
        node = Node(val, neighbors)
        graph.add(node)

    print('main adj_list: {}'.format(graph.adj_list))
    graph.BFS(0)
