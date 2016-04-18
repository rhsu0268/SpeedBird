# this is simple bfs search algorithm on a sample graph


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']
         }


def BFS(graph, start):
	#initialize a set for visited nodes and a list (stack) to keep track of where we are
	visited = []
	queue = [start]

	while queue: 
		# pop the top element
		vertex = queue.pop(0)

		#print(vertex)

		# if the vertex is not in the visited set, add it
		if vertex not in visited:
			visited.append(vertex)

			print('---- visited ----')
			print(visited)
			print('----         ----')

			# add only the unvisited nodes
			queue.extend(set(graph[vertex]) - set(visited))

			# sort the values to make sure that we are doing this alphabetically
			queue.sort()



			print('---- queue ----')
			print(queue)
			print('----       ----')

	return visited

print(BFS(graph, 'A'))


