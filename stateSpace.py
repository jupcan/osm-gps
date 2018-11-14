from lxml import etree
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
        #input: osm node, output: true/false if in nodes
        if id in self._nodes:
            return True
        else:
            return False

    def positionNode(self, id):
        #input: osm node, output: latitude&longitude(y,x) of current node
        try:
            if self.belongNode(id):
                return self._nodes[id]
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")

    def distance(self, node1, node2):
        """
        :param idNode1: node id string
        :param idNode2: node id string
        :return: distance (meters) between idNode1 and idNode2
        """
        (lng1, lat1) = self.positionNode(node1)
        (lng2, lat2) = self.positionNode(node2)
        earth_radius = 6371009

        phi1 = math.radians(float(lat1)); phi2 = math.radians(float(lat2)); d_phi = phi2 - phi1
        theta1 = math.radians(float(lng1)); theta2 = math.radians(float(lng2)); d_theta = theta2 - theta1

        h = math.sin(d_phi/2)**2 +math.cos(phi1)*math.cos(phi2)*math.sin(d_theta/2)**2
        h = min(1.0, h) #protect against floating point errors
        arc = 2*math.asin(math.sqrt(h))

        #return distance in units of earth_radius
        dist = arc*earth_radius
        return dist

    def successors(self, id):
        #input: problem state, output: list of adjacent nodes + extra info
        try:
            successors = []
            if self.belongNode(id._current):
                adjacents = [key for key in self._edges.keys() if id._current in key[0]]
                for data in adjacents:
                    acc = "I'm in %s and I go to %s" % (data[0].zfill(10), data[1].zfill(10))
                    aux = state(data[1], id.visited(data[1], id._nodes)) #creates new ._md5
                    cost = self._edges[data][1]
                    heu = self.distance(data[0], data[1])
                    successors.append((acc, aux, cost, heu))
                return successors
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")
