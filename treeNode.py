from state import state
import random

class treeNode():
	def __init__(self, parent=None, state=None, cost=0, action="", d=0, father=None):
		self.parent = parent
		self._state = state #current state of the problem
		self._cost = cost #cost from the inicial node to the current node (this one)
		self._action = action
		self._d = d #depth of the node.
		self._father = father
		self._f = random.uniform(1, 1000) #random value that determines the insertion order in the frontier
