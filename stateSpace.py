from lxml import etree
from state import state
import math

class stateSpace():
    def __init__(self, path):
        self._path = path
        self._keys, self._nodes, self._edges = self._readFile()
        self._visitedList = []

    def _readFile(self):
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
        #input: problem state, output: true/false if current in nodes
        if id._current in self._nodes:
            return True
        else:
            return False

    def positionNode(self, id):
        #input: problem state, output: latitude&longitude[(y,x)] of current node
        try:
            node_exists = self.belongNode(id)
            if node_exists:
                return [self._nodes[id]]
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")

    def successors(self, id):
        #input: problem state, output: list of adjacent nodes + extra info
        try:
            node_exists = self.belongNode(id)
            successors = []
            if node_exists:
                adjacents = [key for key in self._edges.keys() if id._current in key[0]]
                for data in adjacents:
                    #streets[data] = tuple(self._edges[data])
                    acc = "I'm in %s and I go to %s" % (data[0], data[1])
                    aux = state(data[1], id.visited(data[1], id._nodes))
                    cost = self._edges[data][1]
                    #!(heuristhic)!
                    """orig = [self.positionNode(data[0])[0][0], self.positionNode(data[0])[0][1]]
                    dest = [self.positionNode(data[1])[0][0], self.positionNode(data[1])[0][1]]
                    cost = math.hypot(float(dest[0]) - float(orig[0]), float(dest[1]) - float(orig[1]))"""
                    successors.append((acc, aux, cost))
                    new_md5 =  aux.createCode(aux._current, aux._nodes)
                    print("%s state md5: %s" % (aux._current, new_md5))
                return successors
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")

    def visitedList(self, id):
        #input: problem state, output: visited list
        visited = False
        for data in self._visitedList:
            aux = data
            if self.equals(id, aux):
                visited = True
                if (id._current._f <= aux._current._f):
                    self._visitedList.remove(data)
                    self._visitedList.append(id)
        if not visited: self._visitedList.append(id)

    def equals(self, a, b):
        #input: 2 problem states, output: true if both equals, false otherwise
        if(a._current == b._current and bool(set(a._nodes).difference(b._nodes)) == False): return True
        else: return False
