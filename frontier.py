from state import state
from treeNode import treeNode
import bisect

class frontier():
    def __init__(self):
        self._frontier = self._createFrontier()

    def _createFrontier(self):
            return []

    def insert(self, node):
        if isinstance(node, treeNode):
            bisect.insort(self._frontier, (node._f, node))
        else:
            print("Error. It is not a node")

    def remove(self):
        del self._frontier[0]

    def isEmpty(self):
        if bool(self._frontier): #true if has items, false otherwise
            return False
        else:
            return True
