import csv
import dag


class Pipeline: 
	def __init__ (self):
		self.tasks = dag.DAG()

	def task(self, depends_on = None):
		def inner(f):
			self.tasks.add(f)

			if depends_on: 
				self.tasks.add(depends_on, f)
			return f
		return inner 

	def run(self):
		visited = self.tasks.sort()
		completed = {}

		for task in visited:
			for node, ptr in self.tasks.graph.items():
				if task in ptr:
					completed[task] = task(completed[node])
			if task not in completed:
				completed[task] = task()

		return completed

