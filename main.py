#!/usr/bin/python3
# -*- coding: utf-8 -*-
from graph import graph
import time

def main():
    try:
        filename = input('file: ')
        if filename.isdigit():
            raise ValueError
        town1 = graph('data/%s.graphml.xml' % filename)
        nodes = [i for i in input('node: ').split(',')]
        for node in nodes:
            start_time = time.time()
            print(town1.belongNode(node))
            town1.positionNode(node)
            town1.adjacentNode(node)
            print("%s seconds" % (time.time() - start_time))
            
    except ValueError:
        print ("Error. Not a valid input.")
    
    """town1 = graph('data/anchuras.graphml.xml')
    print(town1.belongNode('4331489627'))
    town1.positionNode('4331489627')
    town1.adjacentNode('4331489627')"""
    
if __name__ == '__main__':
    main()