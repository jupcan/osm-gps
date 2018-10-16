class state():
 
    _current = ""
    _nodes = {}
    _md5 = ""

    def __init__(self, current, nodes, sl):
        self._current = current
        self._nodes = nodes
        self._md5 = sl

    def getNodes(self):
        return self._nodes
