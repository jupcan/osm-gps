from state import state

class stateSpace():
    def __init__(self, path, states):
        self._path = path
        self._states = states

    def successors(self, state):
        acc = {}
        costAct = {}
        return acc, costAct

    def belongNode(self, state):
        #output: True (if it belongs to the State Space) or False(in other case)
        if state in self._states:
            return True
        else:
            return False
