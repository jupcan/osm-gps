from state import state
from treeNode import treeNode
from sortedcontainers import SortedKeyList

class frontier():
    def __init__(self):
        self._frontier = self._createFrontier()

    def _createFrontier(self):
            frontier = SortedKeyList(key=treeNode.getF)
            return frontier

    def insert(self, node):
        if isinstance(node, treeNode):
            self._frontier.add(node)
        else:
            print("error. it is not a node")

    def remove(self):
        return self._frontier.pop(0)

    def isEmpty(self):
        if bool(self._frontier): #true if has items, false otherwise
            return False
        else:
            return True
