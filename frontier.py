from state import state
from treeNode import treeNode
from sortedcontainers import SortedDict

class frontier():
    def __init__(self):
        self._frontier = self._createFrontier()

    def _createFrontier(self):
            frontier = SortedDict()
            return frontier

    def insert(self, node):
        if isinstance(node, treeNode):
            self._frontier[node._f] = node
        else:
            print("Error. It is not a node.")

    def remove(self):
        return self._frontier.popitem(0)

    def isEmpty(self):
        if bool(self._frontier): #true if has items, false otherwise
            return False
        else:
            return True
