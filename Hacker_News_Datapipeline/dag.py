from collections import deque

class DAG:
	
	def __init__(self):
		self.graph = {}


	def in_degree(self):
		indegree = {}

		for node in self.graph:
			if node not in indegree:
				indegree[node] = 0

			for nei in self.graph[node]:
				if nei not in indegree:
					indegree[nei] = 0
				indegree[nei] += 1

		return indegree

	def sort(self):
		to_visit = deque()
		indegree = self.in_degree()

		#to find the node first
		for node in self.graph:
			if indegree[node] == 0:
				to_visit.append(node)

		#sort the graph's node in the order of fewer indegree numbers 
		sorted_node = []

		while to_visit:
			node = to_visit.popleft()

			for nei in self.graph[node]:
				indegree[nei] -= 1
				if indegree[nei] == 0:
					to_visit.append(nei)

			sorted_node.append(node)

		return sorted_node


	def add(self, node, to=None):
		if node not in self.graph:
			self.graph[node] = []

		if to:
			if to not in self.graph:
				self.graph[to] = []

			self.graph[node].append(to)

		if len(self.sort()) != len(self.graph):
			raise Exception 



