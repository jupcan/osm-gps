import hashlib

class state():
    def __init__(self, current, nodes, md5):
        self._current = current
        self._nodes = nodes
        self._md5 = md5

    def createCode(self):
        data = self._current + ''.join(str(i) for i in self._nodes) # _nodes to string
        md5 = hashlib.new("md5", data.encode('utf-8'))
        return md5.hexdigest()

    def getNodes(self):
        return self._nodes

    def __str__(self):
        return f'({self._current}, {self._nodes})'
