INF = 99999999
V = 6

graph = [[0,4,6,0,0,0],
	[4,0,6,3,4,0],
	[6,6,0,1,8,0],
	[0,3,1,0,2,3],
	[0,4,8,2,0,7],
	[0,0,0,3,7,0]]
	
def selectMinVertex(value, setmst):
	minimum = INF
	vertex = None
	for i in range(V):
		if setmst[i] == False and value[i]<minimum:
			vertex = i
			minimum = value[i]
	return vertex
	
def find_mst(graph):
	parent = [0] * V #store MST
	value = [INF] * V #used for edge relaxation
	setmst = [False] * V #True -> vertex included in MST
	
	#Assuming start point as Node->0
	parent[0] = -1 #Start node has no parent 
	value[0] = 0 #start node has value=0 to get picked first
	
	#form MST with (v-1) edges
	for i in range(V-1):
		#select best vertex by applying greedy method
		u = selectMinVertex(value, setmst)
		setmst[u] = True
		
		#Relax adjacent vertices (not yet included in MST)
		for j in range(V):
			'''3 contraints to relax->
			1-> edge is present from u to j
			2-> vertex j is not included in MST
			3-> edge weight is smaller that current edge weight'''
			
			if graph[u][j] != 0 and setmst[j] == False and graph[u][j] < value[j]:
				value[j] = graph[u][j]
				parent[j] = u;
				
	for i in range(1,V):
		print("U->V:{0} -> {1}  weight {2}".format(parent[i], i, graph[parent[i]][i]))
		
find_mst(graph)
	
	
