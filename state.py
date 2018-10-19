import hashlib

class state():
    def __init__(self, current, nodes, md5):
        self._current = current
        self._nodes = nodes
        self._md5 = md5

    def createCode(self):
        data = self._nodes
        code = hashlib.new("md5", data)
        return md5

    def getNodes(self):
        return self._nodes
