from lxml import etree
from os.path import basename
from pprint import pprint

class graph():
    _path = ""
    def __init__(self, path):
        self._path = path
        self._keys, self._nodes, self._edges = self._readFile()

    def _readFile(self):
        data = etree.parse(self._path)
        root = data.getroot()
        ns = {'n': 'http://graphml.graphdrawing.org/xmlns'}

        keys = [] #get desired key values for each file
        nodes, edges = {}, {}
        print(basename(self._path)) #print file name
        for key in root:
            name = key.get('attr.name')
            data_structure = key.get('for')
            if (name == "y" or name == "x") and data_structure == "node":
                id = key.get('id')
                keys.append(id)
            if (name == "length" or name == "name") and data_structure == "edge":
                id = key.get('id')
                keys.append(id)
    
        for node in root.findall('n:graph/n:node', ns):
            id = node.get('id')
            nodes[id] = tuple([data.text for data in node if \
            (data.get('key') == keys[2] or data.get('key') == keys[3])])

        for edge in root.findall('n:graph/n:edge', ns):
            source = edge.get('source')
            target = edge.get('target')
            edges[(source, target)] = tuple([data.text for data in edge if \
            (data.get('key') == keys[0] or data.get('key') == keys[1])])
        return keys, nodes, edges

    def belongNode(self, id):
        #input: osm node id, output: true/false
        if id in self._nodes:
            return True
        else:
            return False

    def positionNode(self, id):
        #input: osm node id, output: latitude&longitude[(y,x)]
        try:
            node_exists = self.belongNode(id)
            if node_exists:
                print([self._nodes[id]])
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")

    def adjacentNode(self, id):
        #input: osm node id, output: list of adjacent arcs
        try:
            node_exists = self.belongNode(id)   
            streets = {}
            if node_exists:
                adjacents = [key for key in self._edges.keys() if id in key[0]]
                for data in adjacents:
                    streets[data] = tuple(self._edges[data])
                pprint(streets)
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")