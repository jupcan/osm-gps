from lxml import etree
from pprint import pprint
from state import state
import math

class stateSpace():
    def __init__(self, path):
        self._path = path
        self._keys, self._nodes, self._edges = self._readFile()

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
        #input: problem state or osm id node, output: true/false if current in nodes
        if isinstance(id, state):
            if id._current in self._nodes: return True
            else: return False
        else:
            if id in self._nodes: return True
            else: return False

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
            streets, successors = {}, []
            if node_exists:
                adjacents = [key for key in self._edges.keys() if id._current in key[0]]
                for data in adjacents:
                    #streets[data] = tuple(self._edges[data])
                    acc = "i'm in %s and i go to %s" %(data[0], data[1])
                    orig = [self.positionNode(data[0])[0][0], self.positionNode(data[0])[0][1]]
                    dest = [self.positionNode(data[1])[0][0], self.positionNode(data[1])[0][1]]
                    cost = math.hypot(float(dest[0]) - float(orig[0]), float(dest[1]) - float(orig[1]))
                    successors.append((acc, data[1], cost))
                return successors
                #pprint(streets)
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")
