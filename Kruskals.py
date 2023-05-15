V = 6
E = 10
dsuf = [-1] * V
mst= [] * (V-1)
edges = [[0,1,1],
	[1,3,1],
	[2,4,1],
	[0,2,2],
	[2,3,2],
	[3,4,2],
	[1,2,3],
	[1,4,3],
	[4,5,3],
	[3,5,4]]
	

	
#printing MST
def printmst():
	print("Minimum spanning tree formed is :\n")
	for edge in mst:
		print("From {0} --> To {1}  Weight ->{2}".format(edge[0], edge[1], edge[2]))
		
	
#finding the absolute parent 
def find(vertex):
	if dsuf[vertex] == -1:
		return vertex
	return find(dsuf[vertex])
	
#making union of two disjoint sets 
def union(fromP, toP):
	fromP = find(fromP)
	toP = find(toP)
	dsuf[fromP] = toP
	
#finds MST using Kruskal's algorithm
def kruskals(edges, V, E):
	edges.sort(key=lambda x: int(x[2]))
	i = 0
	j = 0
	while i<V-1 and j<E :
		fromP = find(edges[j][0])
		toP = find(edges[j][1])
		
		if fromP == toP:
			j = j + 1
			continue
		union(fromP, toP)
		mst.append(edges[j])
		i = i + 1
		
		
kruskals(edges, V, E)
printmst()
