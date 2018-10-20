from state import state
from treeNode import treeNode

class frontier():
    _frontier = {}
    def __init__(self):
        self._frontier = self._createFrontier()

    def _createFrontier(self):
        return _frontier

    def insert(self, node):
        frontier[node.f] = node
