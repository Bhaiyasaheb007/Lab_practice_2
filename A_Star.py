class Graph:
	
	# Constructor 
	def __init__(self, adjacency_list):
		self.adjacency_list = adjacency_list
		
	# Returns list containing tuples with node and weight --> [ ( node, weight) ]
	def get_neighbors(self, v):
		return self.adjacency_list[v]
		
	# Heuristic value for each node --> taken as 1 for all nodes
	def h(self, n):
		heuristic = {
			'A' : 1,
			'B' : 1,
			'C' : 1,
			'D' : 1,
			'E' : 1,
			'G' : 1
		}
		
		return heuristic[n]
		
	# A_star algorithm main logic
	def A_star(self, start_node, goal_node):
	
		# Defining open_list and closed list
		open_list = set([start_node]) # Stores nodes which are visited but neighbors are not inspected
		closed_list = set([]) # stores nodes which are visited and all neighbors are inspected
		
		# Defining dictionary --> stores g value for each node
		g = {}
		g[start_node] = 0 # g value of starting node is zero
		
		# Defining dictionary --> stores parents of ecah node
		parent = {}
		parent[start_node] = start_node # parent of start node is start node itself
		
		
		# Loop open_list until it is empty
		while len(open_list) > 0:
		
			# Initially no node is selected
			n = None
			
			# Select node with minimum f = g + h value from the open_list
			for v in open_list:
				
				if n == None or g[v]+self.h(v) < g[n]+self.h(n):
					n = v
				
			# if no node is selected them path does not exist	
			if n == None:
				print("Path from start node to goal node does not exist")
				return None
				
			# Check if selected node is equal to goal node. if yes then reconstruct the path with parent dictionary
			if n == goal_node:
				path = []
				
				while parent[n] != n:
					path.append(n)
					n = parent[n]
					
				path.append(start_node)
				path.reverse()
				
				print("Path found : {}".format(path))
				return path
				
			# Inspect all the neighbor nodes of selected node (n)
			for (node, weight) in self.get_neighbors(n):
				
				# If neighbor node is not open list and clodes list means it is not visited yet.
				if node not in open_list and node not in closed_list:
					open_list.add(node) # add it to open list 
					parent[node] = n # update its parent
					g[node] = g[n] + weight # update its g value
					
				# Neighbor node is in one of the list 
				else:
					if g[node] > g[n] + weight: 
						g[node] = g[n] + weight # update neighbors g value
						parent[node] = n # update its parent
					
					# nodes g value is updated so, if it is in closed list then reconsider it and add to open list	
					if node in closed_list:
						closed_list.remove(node)
						open_list.add(node)
				
			# add the n(current node ) in closed list as it is visited and its neighbors also inspected totally		
			open_list.remove(n)
			closed_list.add(n)
			
		# if control comes here then path does not exist 
		print("Path does not exist!")
		return None
		
	
	
# Example --> graph representation using adjacency list	
adjacency_list = {
    'A': [('B', 2),('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': [('G', 32)],
    'E': [('D', 6)],
    'D': [('G', 1)],
   
}

# Passing adjacency list while constructing Graph object
my_graph = Graph(adjacency_list)

# Invoking A_star method 
my_graph.A_star('A', 'G')

				
				
			
		
