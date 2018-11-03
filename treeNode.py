from state import state
import random

class treeNode():
	def __init__(self, state, strategy, parent=None, cost=0, action=0, d=0):
			self._parent = parent
			self._state = state #current state of the problem
			self._cost = cost;
			self._d = d
			self._action = action
			self._f = random.uniform(1, 1000) #random value that determines the insertion order in the frontier
