from state import state

class treeNode():
	def __init__(self, state, strategy, parent=None, cost=0, action=None, d=0):
			self._parent = parent
			self._state = state #current state of the problem
			if parent is not None: self._cost = parent._cost+cost; self._d = parent._d+1
			else: self._cost = cost; self._d = d
			self._action = action
			switch = {0: d, 1: -d, 2: -d, 3: -d, 4: cost, 5: cost}
			self._f = switch[strategy]

	def getF(self):
		return self._f
