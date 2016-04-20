# Uniform Cost Search


# sample graph 

graph = {
	
	'A': [['B', 250], ['C', 270]],
	'B': [['B', 250], ['C', 300]],
	'C': [['A', 270], ['D', 300]],
	'D': [['C', 420]]
}

def uniform_cost_search(graph, start, goal):
	node = start

	# initialize the cost
	cost = 0

	# initialize a queue containing node only
	frontier = [node]
	print(frontier)
	print(len(frontier))

	# initialize a queeu containing the visited nodes
	visited = []

	while True: 
		print(len(frontier))
		if len(frontier) == 0:
			print("Sorry, no path exists!")
			return 
		# choose the lowest cost node from the frontier
		node = frontier.pop()

		if node == goal:
			print("You reached the goal!")
			return visited
		# add that node to the visited nodes queue
		visited.append(node)

		count = 0

		# for each of the node's neighbors n 
		# for neighbor in graph[node]:
		# 	print(neighbor)

		# 	# if neighbor is goal, then we have reached it
		# 	# if neighbor[0] == goal:
		# 	# 	print("You reached the goal!")
		# 	# 	return frontier

		# 	# check that it is not in the visited
		# 	if neighbor[0] not in visited:
		# 		# check that it is not in the frontier
		# 		if neighbor[0] not in frontier:
		# 			frontier.append(neighbor)
		# 			stored_cost = neighbor[1]
		# 			#print(cost)
		# 			#print(frontier)
		# 		elif neighbor[1] > stored_cost:
		# 			# remove the node in frontier
		# 			frontier.pop()
		# 			# add the new node with the lower cost
		# 			frontier.append(neighbor)
		#return frontier

print(uniform_cost_search(graph, 'A', 'D'))
	