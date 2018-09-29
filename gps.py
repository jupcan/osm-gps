from lxml import etree

def main():
    data = etree.parse('data/navalpino.graphml.xml')
    root = data.getroot()
    ns = {'n': 'http://graphml.graphdrawing.org/xmlns'}
    
    nodes = [node.get('id') for node in root.findall('n:graph/n:node', ns)]
    print(belongNode(nodes,'950073335'))

def belongNode(nodes,id):
    #input: osm node id, output: true/false
    try:
        nodes.index(id) 
    except ValueError:
        return False
    else:
        return True

if __name__ == '__main__':
    main()