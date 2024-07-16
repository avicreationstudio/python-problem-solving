graph = {
	1: [2,4],
	2: [3,5],
	3: [],
	4: [6],
	5: [6],
	6: []
}


def bft(graph,node):
	# breath first traversal
	queue = []
	visited = set()

	queue.append(node)
	while queue:
		node = queue.pop(0)
		print(node,end=" ")
		for neighbour in graph[node]:
			if neighbour not in visited:
				queue.append(neighbour)
				visited.add(neighbour)
		

visited = set()

def dft(graph,node):
	# depth first traversal
	if node not in visited:
		print(node,end=" ")
		visited.add(node)
		for neighbour in graph[node]:
			dft(graph,neighbour)

print("bft")
bft(graph,1)

print()

print("dft")
dft(graph,1)
