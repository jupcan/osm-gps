from state import state
from treeNode import treeNode
from sortedcontainers import SortedKeyList

class frontier():
    def __init__(self):
        self._frontier = self._createFrontier()

    def _createFrontier(self):
        """
        :return: frontier data structure
        """
        frontier = SortedKeyList(key=treeNode.getF)
        return frontier

    def insert(self, node):
        """
        inserts node into the frontier
        :param node: node id string to insert
        """
        if isinstance(node, treeNode):
            self._frontier.add(node)
        else:
            print("error. it is not a node")

    def remove(self):
        """
        removes node from the frontier
        :return: node id string removed
        """
        return self._frontier.pop(0)

    def isEmpty(self):
        """
        :return: true/false if elements in the frontier
        """
        if bool(self._frontier): return False
        else: return True
