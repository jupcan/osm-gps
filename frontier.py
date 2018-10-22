from state import state
from treeNode import treeNode

class frontier():
    def __init__(self):
        self._frontier = self._createFrontier()

    def _createFrontier(self):
            return {}

    def insert(self, node):
        if(type(node) is treeNode):
            self._frontier[node] = hex(id(node)) #convert object id to hex to see it better
            self._frontier = self.sortFrontier()
        else:
            print("Is not a node")

    def remove(self):
        del self._frontier[min(self._frontier)]

    def isEmpty(self):
        if bool(self._frontier): #true if has items, false otherwise
            return False
        else:
            return True

    def sortFrontier(self):
        return dict(sorted(self._frontier.items()))
