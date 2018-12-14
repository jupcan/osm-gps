from lxml import etree
from state import state
import sys

class stateSpace():
    def __init__(self, path):
        self._path = path
        self._keys, self._nodes, self._edges = self._readFile()

    def _readFile(self):
        """
        :return: data from xml loaded into data structures
        """
        data = etree.parse(self._path)
        root = data.getroot()
        ns = {'n': 'http://graphml.graphdrawing.org/xmlns'}

        keys, nodes, edges = {}, {}, {}
        for key in root: #get desired key values for each file
            keys[(key.get('attr.name'), key.get('for'))] = (key.get('id'))
        key_y = keys[('y', 'node')]
        key_x = keys[('x', 'node')]
        key_name = keys[('name', 'edge')]
        key_length = keys[('length', 'edge')]

        for node in root.findall('n:graph/n:node', ns):
            data = dict((d.get('key'), d.text) for d in node)
            values = (data.get(key_y), data[key_x])
            nodes[node.get('id')] = values

        for edge in root.findall('n:graph/n:edge', ns):
            data = dict((d.get('key'), d.text) for d in edge)
            values = (data.get(key_name, 'sinNombre'), data[key_length])
            edges[(edge.get('source'), edge.get('target'))] = values
        return keys, nodes, edges

    def belongNode(self, id):
        """
        :param id: osm node id string
        :return: true/false if in nodes
        """
        if id in self._nodes: return True
        else: return False

    def positionNode(self, id):
        """
        :param id: osm node id string
        :return: latitude&longitude(y,x) of the node
        :raises ValueError: not entering a valid node id
        """
        try:
            if self.belongNode(id):
                return self._nodes[id]
            else:
                raise ValueError
        except ValueError:
            print("error. the node does not exist"); sys.exit(1)

    def successors(self, id):
        """
        :param id: state class object
        :return: list of successors for given state + info(acc,aux,cost)
        :raises ValueError: not entering a valid state for given json
        """
        try:
            successors = []
            if self.belongNode(id._current):
                adjacents = [key for key in self._edges.keys() if id._current in key[0]]
                for data in adjacents:
                    acc = "I'm in %s and I go to %s c/%s" % (data[0].zfill(10), data[1].zfill(10), self._edges[data][0])
                    aux = state(data[1], id.visited(data[1], id._nodes)) #creates new ._md5
                    cost = self._edges[data][1]
                    successors.append((acc, aux, cost))
                return successors
            else:
                raise ValueError
        except ValueError:
            print("error. the state does not belong to given json"); sys.exit(1)
