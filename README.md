# osm-gps
**a3 group** intelligent systems lab project
> designment and developement of an agent program to find the optimal route for a vehicle that circulates through a set of places of a town using data from open street map - [uclm](https://www.uclm.es/) computer science | [osm](https://www.openstreetmap.org) grahml data

## task1
given a file in format grahml, the students must write a class ”graph” containing:
- a constructor, that receives as parameter the name of the file graphml
- methods: belongNode, positionNode and adjacentNode

below we are showing a command line output example for the 3 aforementioned methods:

```python
file: ciudad real.graphml.xml
nodes: 796725819,765309509,827212358
True
[('38.9845189', '-3.9145536')]
{('796725819', '764039286'): ('Avenida de Europa', '4.148'),
 ('796725819', '797147422'): ('Calle Santa María de Alarcos', '9.129')}
0.0005040168762207031 seconds
True
[('38.9849254', '-3.9246998')]
{('765309509', '803292210'): ('Calle de la Mata', '38.067')}
0.0003075599670410156 seconds
True
[('38.9828974', '-3.9395137')]
{('827212358', '827212360'): ('Calle Goya', '47.442'),
 ('827212358', '827212476'): ('Calle Atalaya', '42.912')}
0.0003237724304199219 seconds


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

        keys, nodes, edges = {}, {}, {}
        print(basename(self._path)) #print file name
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
```
