from state import state
from treeNode import treeNode
import bisect
import heapq

class frontier():
    def __init__(self):
        self._frontier = self._createFrontier()

    def _createFrontier(self):
            frontier = []
            heapq.heapify(frontier)
            return frontier

    def insert(self, node):
        if isinstance(node, treeNode):
            heapq.heappush(self._frontier, (node._f, node))
        else:
            print("Error. It is not a node.")

    def remove(self):
        return heapq.heappop(self._frontier)

    def isEmpty(self):
        if bool(self._frontier): #true if has items, false otherwise
            return False
        else:
            return True
