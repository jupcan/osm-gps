import hashlib

class state():
    def __init__(self, current, nodes, md5=None):
        self._current = current
        self._nodes = sorted(nodes)
        if md5 is None: self._md5 = self.createCode(self._current, self._nodes)
        else: self._md5 = md5

    def createCode(self, node, list):
        """
        :param node: current node id string
        :param list: nodes' list to be visited
        :return: md5 representation of a state
        """
        data = node + ''.join(str(i) for i in list) #_current + _nodes to string
        md5 = hashlib.new("md5", data.encode('utf-8')) #encode string
        return md5.hexdigest() #return hexadecimal string value

    def visited(self, id, old_list):
        """
        :param id: node id string
        :param old_list: old nodes' list to be visited
        :return: new list removing current or just the old one
        """
        if id in old_list:
            new_list = old_list[:]
            new_list.remove(id)
            return new_list
        else:
            return old_list

    def updateCode(self, aux):
        """
        updates md5 representation of a state
        :param aux: state class auxiliar object
        """
        self._md5 = self.createCode(aux._current, aux._nodes)

    def __str__(self):
        """
        :return: state to string
        """
        return f'({self._current}, {self._nodes})'
