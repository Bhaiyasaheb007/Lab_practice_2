from collections import deque

Graph = {
	'A':['B','C'],
	'B':['A','D'],
	'C':['A','D','E'],
	'D':['B','C','E'],
	'E':['C','D']
}

start_node = 'A' #root node

# keep track of visited elements
visited = set([start_node])

#queue for storing neighbours to visit in order
queue = deque([start_node])

# bfs function
def bfs(Graph, visited, queue):
	# if queue is empty means all vertices are visited
	if not queue:
		return 
		
	# else case pop element from queue and explore its neighbour
	vertex = queue.popleft()
	print(vertex)
	
	#for each neighbour of vertex
	for neighbour in Graph[vertex]:
		#if it is not visited already then add it to visited and queue
		if neighbour not in visited:
			visited.add(neighbour)
			queue.append(neighbour)
			
	#recursive call
	bfs(Graph, visited, queue)
	
bfs(Graph, visited, queue)
		
		
