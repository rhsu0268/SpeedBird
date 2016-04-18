# this is simple dfs search algorithm on a sample graph


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']
         }

def DFS(graph, start):
	#initialize a set for visited nodes and a list (stack) to keep track of where we are
	visited = []
	stack = [start]

	while stack: 
		# pop the top element
		vertex = stack.pop()

		#print(vertex)

		# if the vertex is not in the visited set, add it
		if vertex not in visited:
			visited.append(vertex)

			print('---- visited ----')
			print(visited)
			print('----         ----')

			# add only the unvisited nodes
			stack.extend(set(graph[vertex]) - set(visited))



			print('---- stack ----')
			print(stack)
			print('----       ----')

	return visited



result = DFS(graph, 'A')
print(result)

# graph = {
	
# 	0: [1, 5],
# 	1: [0, 2, 3],
# 	2: [1, 4],
# 	3: [1, 4, 5],
# 	4: [2, 3, 5],
# 	5: [0, 3, 4]
# }


# def dfs(graph, root):
# 	visited = []
# 	stack = [root]
# 	while stack:
# 		node = stack.pop()
# 		print(node)

# 		if node not in visited:
# 			visited.append(node)

# 			stack.extend([x for x in graph[node] if x not in visited])
# 	return visited

#print(dfs(graph, 0))