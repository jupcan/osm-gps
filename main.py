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
        nodes = [i for i in input('nodes: ').split(',')]
        for node in nodes:
            start_time = time.time()
            print(town1.belongNode(node))
            town1.positionNode(node)
            town1.adjacentNode(node)
            print("%s seconds" % (time.time() - start_time))
    except ValueError:
        print ("Error. Not a valid input.")
    
if __name__ == '__main__':
    main()