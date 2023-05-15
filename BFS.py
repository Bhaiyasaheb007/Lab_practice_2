
import collections
def bfs(graph, root):
	visited = set()
	queue = collections.deque([root])
	
	while queue:
		vertex = queue.popleft()
		visited.add(vertex)
		for adj in graph[vertex]:
			if adj not in visited:
				queue.append(adj)
	print(visited)
				
		

graph= {
	0:[1,2,3], 1:[0,2], 2:[0,1,4], 3:[0], 4:[2]
}

bfs(graph,0)


