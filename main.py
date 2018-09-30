from lxml import etree

def main():
    data = etree.parse('data/navalpino.graphml.xml')
    root = data.getroot()
    ns = {'n': 'http://graphml.graphdrawing.org/xmlns'}
    
    nodes = []
    for node in root.findall('n:graph/n:node',ns):
        id = node.get('id')
        nodes.append((id, *(data.text for data in node if data.get('key') != 'd6')))
    #print(nodes)

    print(belongNode(nodes,'950073331')[0])
    positionNode(nodes,'950073331')

def belongNode(nodes,id):
    #input: osm node id, output: true/false
    node_exists = False
    for data in nodes:
        if data[0] == id:
            node_exists = True
    if node_exists:
        coordinates = (data[1],data[2])
        return True, coordinates
    else:
        return False, False

def positionNode(nodes,id):
    #input: osm node id, output: latitude&longitude 
    try:
        node_exists, coordinates = belongNode(nodes,id)
        if node_exists:
            print(coordinates)
        else:
            raise ValueError
    except ValueError:
        print("Error. The node does not exist.")

if __name__ == '__main__':
    main()