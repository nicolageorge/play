from collections import defaultdict
from collections import deque

# directed graph using adjacency list representation
class Graph:
    def __init__(self):
        # dict to store graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # print BFS of graph
    def bfs(self, s):
        visited = [False for _ in range(len(self.graph))]
        queue = deque()

        #mark source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # dequeue vertex and print it
            s = queue.leftpop()
            print s

            # get all adjacent vertices from dequeued vertex s.
            # If an adjaicent has not been visited, mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def dfs_visit(v, visited):
        # mark current node as visited and print it
        visited[v] = True
        print vs

        # recurr on all unvisited vertices adjaicent to vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_visit(i, visited)

    def dfs(self, v):
        # mark all verices as not visited
        visited = [False for _ in range(len(self.graph))]

        # call recursive function to print dfs traversal
        self.dfs_visit(v, visited)
