import hashlib

class state():
    def __init__(self, current, nodes, md5=None):
        self._current = current
        self._nodes = sorted(nodes)
        if md5 is None: self._md5 = self.createCode()
        else: self._md5 = md5

    def createCode(self):
        #_current + _nodes to string
        data = self._current + ''.join(str(i) for i in self._nodes)
        md5 = hashlib.new("md5", data.encode('utf-8')) #encode string
        return md5.hexdigest() #return hexadecimal string value

    def getNodes(self):
        return self._nodes

    def __str__(self):
        return f'({self._current}, {self._nodes})'
