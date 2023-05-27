 # example graph
Graph = [[0,1,1,0,0],
	[1,0,0,1,0,],
	[1,0,0,1,1],
	[0,1,1,0,1],
	[0,0,1,1,0]]
	
N = 5 # number of vertices
M = 3 # number pf colors

#helper function to check color assignment is safe or not
def isSafe(node, color, graph, N, col):
	# check each neighbour of node for color col
	for k in range(N):
		#neighbour has same color
		if k != node and graph[k][node] == 1 and color[k] == col:
			return False
	return True

#recursive function
def solve(node, color, graph, M, N):
	# if node is last node then graph is colored
	if node == N:
		return True
		
	#check for each color it can be assigned to node or not
	for col in range(1, M+1):
		#check color is safe or not
		if isSafe(node, color, graph, N, col):
			color[node] = col # assign color to node
			#check for next node
			if solve(node+1, color, graph, M, N):
				return True
			#backtrack
			color[node] = 0
			

# driver function
def GraphColoring(graph, M, N):
	# stores color assigned to each node
	color = [0] * N
	#call to recursive function to check graph can be colored or not
	if solve(0, color, graph, M, N):
		return True
	return False
	
print(GraphColoring(Graph, M ,N))
