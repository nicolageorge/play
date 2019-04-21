class Node:
	def __init__(self, value, neighbors=None):
		self.value = value
		if(type(neighbors) == 'list'):
			self.neighbors = neighbors
		elif(type(neighbors) == 'string'):
			self.neighbors = neighbors.split(',')

	def add_neighbor(self, node):
		self.neighbors.append(node)


class UndirectedGraph:
	def __init__(self):
		self.nodes = []

	def add(self, node):
		self.nodes.append(node)

	def __str__(self):
		return ', '.join([n.value for n in self.nodes])


if __name__ == '__main__':
	inp = input()
	args = inp.split('#')
	graph = UndirectedGraph()
	for n in args:
		nod = n.split(',')
		val = nod[0]
		neighbors = nod[1:]
		node = Node(val, neighbors)
		graph.add(node)

	print(graph)