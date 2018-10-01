from lxml import etree

class graph():
    _path=""
    _nodes = []
    def __init__(self,path):
        self._path=path
        self._nodes=self._readFile()

    def _readFile(self):
        data = etree.parse(self._path)
        root = data.getroot()
        ns = {'n': 'http://graphml.graphdrawing.org/xmlns'}
    
        nodes = []
        for node in root.findall('n:graph/n:node',ns):
            id = node.get('id')
            nodes.append((id, *(data.text for data in node if data.get('key') != 'd6')))
        #print(nodes)
        return nodes

    def belongNode(self,id):
        #input: osm node id, output: true/false
        node_exists = False
        for data in self._nodes:
            if data[0] == id:
                node_exists = True
        if node_exists:
            coordinates = [(data[1],data[2])]
            return True, coordinates
        else:
            return False, False

    def positionNode(self,id):
        #input: osm node id, output: latitude&longitude 
        try:
            node_exists, coordinates = self.belongNode(id)
            if node_exists:
                print(coordinates)
            else:
                raise ValueError
        except ValueError:
            print("Error. The node does not exist.")