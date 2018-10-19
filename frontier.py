from treeNode import treeNode
from state import state

class frontier():
    def __init__(self):
        self._frontier = self._createFrontier()

    def createFrontier(self):
        frontier = {}

    def insert(self, treeNode):
        frontier[treeNode.f] = treeNode
