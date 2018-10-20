from state import state
from treeNode import treeNode

class frontier():
    _frontier = {}
    def __init__(self):
        self._frontier = self._createFrontier()

    def _createFrontier(self):
        return self._frontier

    def insert(self, node):
        self._frontier[node.getF()] = node

    def isEmpty(self):
        if bool(self._frontier): #bool(<dictionary>) -> true if has items, false otherwise
            return False
        else:
            return True

    def __str__(self):
        return f'{self._frontier}'
