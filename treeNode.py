from state import state

class treeNode():
	def __init__(self, state, strategy, parent=None, cost=0, action=None, h=0, d=1):
		self._state = state #current state of the problem
		self._strategy = strategy
		self._parent = parent
		if parent is not None: self._cost = parent._cost+cost; self._d = parent._d+1
		else: self._cost = cost; self._d = d
		self._action = action
		self._h = h
		switch = {0: d, 1: -d, 2: -d, 3: -d, 4: self._cost, 5: h, 6: h+self._cost}
		self._f = switch[strategy] #factory pattern

	def getF(self):
		return self._f
