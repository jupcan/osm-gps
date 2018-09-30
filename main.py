from lxml import etree

def main():
    data = etree.parse('data/navalpino.graphml.xml')
    root = data.getroot()
    ns = {'n': 'http://graphml.graphdrawing.org/xmlns'}
    
    nodes = []
    for node in root.findall('n:graph/n:node',ns):
        id = node.get('id')
        nodes.append((id, *(data.text for data in node if data.get('key') != 'd6')))
    print(nodes)
    print("------------------------------")

    print(belongNode(nodes,'950073335'))
    positionNode(nodes,'950073335')

def belongNode(nodes,id):
    #input: osm node id, output: true/false
    try:
        nodes.index(id) 
    except ValueError:
        return False
    else:
        return True

def positionNode(nodes,id):
    #input: osm node id, output: latitude&longitude 
    try:
        for data in nodes:
            if data[0] == id:
                print((data[1],data[2]))
    except ValueError:
        print("Error. The node does not exist.")
        return False
    else:
        return True

if __name__ == '__main__':
    main()