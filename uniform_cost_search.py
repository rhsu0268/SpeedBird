# Uniform Cost Search


# sample graph 


# graph = {
	
# 	'A': [['B', 10], ['C', 270]],
# 	'B': [['A', 10], ['C', 20]],
# 	'C': [['A', 270], ['B', 20], ['D', 420]],
# 	'D': [['C', 420], ['E', 125]],
# 	'E': [['D', 125]]
# }


graphWithDirect = {
	
	'JFK': [['SFO', 2566], ['LAX', 2458], ['MSP', 1009], ['ORD', 720], ['CLT', 545], 
	['ATL', 762], ['DFW', 1380], ['SLC', 1970], ['PHX', 2139], ['DTW', 485], ['SEA', 2397]],
	'SFO': [['JFK', 2566], ['LAX', 339], ['MSP', 1586], ['ORD', 1847], ['PHX', 652], 
	['ATL', 2135], ['DFW', 1468], ['SLC', 599], ['DTW', 2083], ['SEA', 679]],
	'LAX': [['JFK', 2458], ['SFO', 339]],
	'MSP': [['JFK', 1009], ['SFO', 1586]],
	'ORD': [['JFK', 720], ['SFO', 1847], ['PHX', 1440]],
	'CLT': [['JFK', 545], ['SFO', 2292]],
	'ATL': [['JFK', 762], ['SFO', 2135]],
	'DFW': [['JFK', 762], ['SFO', 1468]],
	'SLC': [['JFK', 1970], ['SFO', 599]],
	'PHX': [['JFK', 2139], ['SFO', 652], ['ORD', 1440]],
	'DTW': [['JFK', 485], ['SFO', 2083]], 
	'SEA': [['JFK', 2397], ['SFO', 679]]



}

graphWithoutDirect = {
	
	'JFK': [['LAX', 2458], ['MSP', 1009], ['ORD', 720], ['CLT', 545], 
	['ATL', 762], ['DFW', 1380], ['SLC', 1970], ['PHX', 2139], ['DTW', 485], ['SEA', 2397]],
	'SFO': [['LAX', 339], ['MSP', 1586], ['ORD', 1847], ['PHX', 652], 
	['ATL', 2135], ['DFW', 1468], ['SLC', 599], ['DTW', 2083], ['SEA', 679]],
	'LAX': [['JFK', 2458], ['SFO', 339]],
	'MSP': [['JFK', 1009], ['SFO', 1586]],
	'ORD': [['JFK', 720], ['SFO', 1847], ['PHX', 1440]],
	'CLT': [['JFK', 545], ['SFO', 2292]],
	'ATL': [['JFK', 762], ['SFO', 2135]],
	'DFW': [['JFK', 762], ['SFO', 1468]],
	'SLC': [['JFK', 1970], ['SFO', 599]],
	'PHX': [['JFK', 2139], ['SFO', 652], ['ORD', 1440]],
	'DTW': [['JFK', 485], ['SFO', 2083]], 
	'SEA': [['JFK', 2397], ['SFO', 679]]



}





def uniform_cost_search(graph, start, goal):
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

			first_cost = frontier_node_costs[0]
			index = 0
			loop_counter = 0
			for cost in frontier_node_costs[1:len(frontier_node_costs)]:
				print(cost)
				if (cost < first_cost):
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
			if neighbor[0] == goal:
				print("You reached the goal!")
				visited.append(neighbor[0])
				return visited

			# check that it is not in the visited
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

#print(uniform_cost_search(graphWithDirect, 'JFK', 'SFO'))
print(uniform_cost_search(graphWithoutDirect, 'JFK', 'SFO'))

	