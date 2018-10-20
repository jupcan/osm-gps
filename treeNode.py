from state import state

class treeNode():
	f = 0
	def __init__(self, state, cost, action, d):
		self._state = state #current state of the problem
		self._cost = 0 #cost from the inicial node to the current node (this one)
		self._action = ""
		self._d = 0 #depth of the node.
		self.f = random.uniform(1, 1000) #random value that determines the insertion order in the frontier
                
