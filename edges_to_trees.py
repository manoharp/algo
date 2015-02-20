from collections import defaultdict

class Graph(object):
	def __init__(self):
		self.vertices = defaultdict()
		self.parent = defaultdict()

	def add_edge(self, x, y):
		if x not in self.vertices:
			self.vertices[x] = TreeNode(x)
		vert_x = self.vertices[x]

		if y not in self.vertices:
			self.vertices[y] = TreeNode(y)
		vert_y = self.vertices[y]

		# Add adjancents
		vert_x.add_adj(vert_y)

		# Check parent
		if y in self.parent:
			raise ValueError("Can't have two parents! Me: {0} " + \
								"Parent: {1} New Parent:{2}".format(vert_y, self.parent[y], vert_x))
		else:
			self.parent[y] = x

class TreeNode(object):
	def __init__(self, value, *adj_list):
		self.value = value
		self.adj_list = [] if len(adj_list) == 0 else adj_list

	def __str__(self):
		return str(self.value)

	def add_adj(self, node):
		if len(self.adj_list) >= 2:
			raise ValueError("Can't add more than two adjacents Node: " + \
									"{0} Existing : {1} Adding: {2}".format(self.value, self.adj_list, node))

		self.adj_list.append(node)

if __name__ == "__main__":
	g = Graph()
	edges = [(0,1), (1,2), (1,3), (2,4), (2,5), (3,10), (3,11), (10,0)]
	for e in edges:
		g.add_edge(*e)

	root = set(g.vertices.keys()) - set(g.parent.keys())
	if len(root) == 0: 
		print "Sorry! No root found"
	elif len(root) > 1: 
		print "**Evil laugh. Have more than one root"
	else:
		# Go DFS or BFS!
		print root

	
	
