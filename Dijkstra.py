INF = 99999999
V = 6

graph = [[0,4,6,0,0,0],
	[4,0,6,3,4,0],
	[6,6,0,1,8,0],
	[0,3,1,0,2,3],
	[0,4,8,2,0,7],
	[0,0,0,3,7,0]]
	
def selectMinVertex(value, processed):
	minimum = INF
	vertex = None
	for i in range(V):
		if processed[i] == False and value[i]<minimum:
			vertex = i
			minimum = value[i]
	return vertex
	
def dijkstra(graph):
	parent = [0] * V #store SPG
	value = [INF] * V #Keeps shortest path values to each vertex from source
	processed = [False] * V #TRUE->Vertex is processed
	
	#Assuming start point as Node->0
	parent[0] = -1 #Start node has no parent 
	value[0] = 0 #start node has value=0 to get picked first
	
	#Include (V-1) edges to cover all V-vertices
	for i in range(V-1):
		#select best vertex by applying greedy method
		u = selectMinVertex(value, processed)
		processed[u] = True #Include new Vertex in shortest Path Graph
		
		#Relax adjacent vertices (not yet included in shortest path graph)
		for j in range(V):
			'''3 conditions to relax:-
			      1.Edge is present from U to j.
			      2.Vertex j is not included in shortest path graph
			      3.Edge weight is smaller than current edge weight'''
			
			if graph[u][j] != 0 and processed[j] == False and value[u]!=INF and value[u]+graph[u][j] < value[j]:
				value[j] = value[u]+graph[u][j]
				parent[j] = u;
			
	#printing shortest path graph	
	for i in range(1,V):
		print("U->V:{0} -> {1}  weight {2}".format(parent[i], i, graph[parent[i]][i]))
		
dijkstra(graph)


#IME COMPLEXITY: O(V^2)
#TIME COMPLEXITY: (using Min-Heap + Adjacency_List): O(ElogV)
