# Uniform Cost Search


# sample graph 

graph = {
	
	'A': [['B', 10], ['C', 50]],
	'B': [['A', 10], ['C', 20]],
	'C': [['A', 50], ['B', 20], ['D', 420]],
	'D': [['C', 420], ['E', 125]],
	'E': [['D', 125]]
}


straight_line_distance_from_A_to_D = {
	
	'A': 460,
	'B': 420,
	'C': 420,
	'D': 0,
	'E': 125
}



def A_star_search(graph, start, goal):
	node = start

	# initialize the cost
	cost = 0

	frontier = []

	# create a list for all the frontier node
	frontier_node_costs = []

	count = 0

	stored_cost = 0

	# initialize a queue containing node only
	frontier.append(node)
	#print(frontier)
	#print(len(frontier))

	# initialize a queeu containing the visited nodes
	visited = []

	while True: 
		
		# reset count
		count = 0
		#print(len(frontier))
		if len(frontier) == 0:
			print("Sorry, no path exists!")
			return 

		# choose the lowest cost node from the frontier
		if len(frontier_node_costs) != 0:

			first_cost = frontier_node_costs[0] + straight_line_distance_from_A_to_D[frontier[0]]
			print(first_cost)
			index = 0
			loop_counter = 0

			heuristic_cost = 0

			# need to calculate f(n) from cost and estimated cost to goal

			for cost in frontier_node_costs[1:len(frontier_node_costs)]:
				heuristic_cost = cost + straight_line_distance_from_A_to_D[frontier[index]]
				#print(straight_line_distance_from_A_to_D[frontier[index]])
				print(heuristic_cost)
				if (heuristic_cost < first_cost):
					index = loop_counter
				loop_counter += 1
		
			node = frontier.pop(index)
		else:
			node = frontier.pop()

		if node == goal:
			print("You reached the goal!")
			return visited
		# add that node to the visited nodes queue
		visited.append(node)
		print("--- Visited ---")
		print(visited)
		print("--- ---")
		

		#for each of the node's neighbors n 
		for neighbor in graph[node]:
			print("--- Neighbor ---")
			print(neighbor)
			print("--- ---")

			#if neighbor is goal, then we have reached it
			# we eliminate the case of moving further wehn we are done
			if neighbor[0] == goal:
				print("You reached the goal!")
				visited.append(neighbor[0])
				return visited

			# check that it is not in the visited
			# this prevents us from considering a node that we have already visited
			if neighbor[0] not in visited:
				# if this is the first iteration, add the node to the frontier
				if neighbor[0] not in frontier:
					frontier.append(neighbor[0])
					frontier_node_costs.append(neighbor[1])
					cost = neighbor[1]
				elif cost > neighbor[1]:
					frontier.pop()
					frontier.append(neighbor[0])
					frontier_node_costs.append(neighbor[1])
			print("--- Frontier ---")
			print(frontier)
			print("--- ---") 
			# increment counter
			#count = count + 1

print(A_star_search(graph, 'A', 'D'))
	