from state import state

class stateSpace():
    def __init__(self, path, state):
        self._path = path
        self._states = state

    def successors(self, state):
        acc = "i'm in %s and i go to %s" %(state._current, state._nodes[0])
        costAct = 0
        return acc, costAct

    def belongNode(self, state):
        #output: True (if it belongs to the State Space) or False(in other case)
        if state in self._states:
            return True
        else:
            return False
