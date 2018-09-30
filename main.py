from lxml import etree

def main():
    data = etree.parse('data/navalpino.graphml.xml')
    root = data.getroot()
    ns = {'n': 'http://graphml.graphdrawing.org/xmlns'}
    
    nodes = [node.get('id') for node in root.findall('n:graph/n:node',ns)]
    """nodes = []
    for node in root.findall('n:graph/n:node',ns):
        id = node.get('id')
        for data in root.findall('n:graph/n:node/n:data', ns):
            key = data.get('key')
        nodes.append((id,key,"hola"))
    print(nodes)"""

    print(belongNode(nodes,'950073335'))
    positionNode(nodes,id)

def belongNode(nodes,id):
    #input: osm node id, output: true/false
    try:
        nodes.index(id) 
    except ValueError:
        return False
    else:
        return True

def positionNode(nodes,id):
    #input: osm node id, output: longitude&latitude of given node
    try:
        nodes.index(id) 
    except ValueError:
        print("Error. The node does not exist.")
        return False
    else:
        return True

if __name__ == '__main__':
    main()