import hashlib

class state():
    def __init__(self, current, nodes, md5=None):
        self._current = current
        self._nodes = sorted(nodes)
        if md5 is None: self._md5 = self.createCode(self._current, self._nodes)
        else: self._md5 = md5

    def createCode(self, node, list):
        #_current + _nodes to string
        data = node + ''.join(str(i) for i in list)
        md5 = hashlib.new("md5", data.encode('utf-8')) #encode string
        return md5.hexdigest() #return hexadecimal string value

    def getNodes(self):
        return self._nodes

    def visited(self, id, old_list):
        if id in old_list:
            new_list = old_list[:]
            new_list.remove(id)
            return new_list
        else:
            return old_list

    def __str__(self):
        return f'({self._current}, {self._nodes})'
