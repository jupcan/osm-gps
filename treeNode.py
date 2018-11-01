from state import state
import random

class treeNode():
	def __init__(self, state, parent=None, cost=0, action=0, d=0):
			self._parent = parent
			self._state = state #current state of the problem
			if(parent != None):
				self._cost = parent._cost + cost#cost from the inicial node to the current node (this one)
				self._d = parent._d+1#depth of the node.
			else:
				self._cost = cost
				self._d = d
			self._action = action
			self._f = random.uniform(1, 1000) #random value that determines the insertion order in the frontier
