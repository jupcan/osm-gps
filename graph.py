from lxml import etree

class graph():
    _path = ""
    _nodes = []
    def __init__(self, path):
        self._path = path
        self._nodes, self._edges = self._readFile()

    def _readFile(self):
        data = etree.parse(self._path)
        root = data.getroot()
        ns = {'n': 'http://graphml.graphdrawing.org/xmlns'}
    
        nodes = []
        for node in root.findall('n:graph/n:node', ns):
            id = node.get('id')
            nodes.append((id, *(data.text for data in node if (data.get('key') == 'd4' or data.get('key') == 'd5'))))

        edges = []
        for edge in root.findall('n:graph/n:edge', ns):
            source = edge.get('source')
            target = edge.get('target')
            edges.append((source, target, *(data.text for data in edge if (data.get('key') == 'd13' or data.get('key') == 'd11'))))
        return nodes, edges

    def belongNode(self, id):
        #input: osm node id, output: true/false
        node_exists = False
        for data in self._nodes:
            if data[0] == id:
                node_exists = True
            if node_exists:
                coordinates = [(data[1], data[2])]
                return True, coordinates
        return False, False

    def positionNode(self, id):
        #input: osm node id, output: latitude&longitude[(y,x)]
        try:
            node_exists, coordinates = self.belongNode(id)
            if node_exists:
                print(coordinates)
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")

    def adjacentNode(self, id):
        #input: osm node id, output: list of adjacent arcs
        try:
            adjacents = []
            node_exists = self.belongNode(id)[0]
            if node_exists:
                for data in self._edges:
                    if data[0] == id:
                        edge_info = (data[0:4])
                        adjacents.append(edge_info)
                print(*adjacents, sep="\n" )
                #print(adjacents)
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")