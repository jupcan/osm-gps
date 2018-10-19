import hashlib

class state(): 
    def __init__(self, current, nodes, code):
        self._current = current
        self._nodes = nodes
        self._md5 = code

    def createCode(self):
        data = self._nodes
        code = hashlib.new("md5", data)
        return code

    def getNodes(self):
        return self._nodes
