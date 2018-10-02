#!/usr/bin/python3
# -*- coding: utf-8 -*-
from graph import graph
import time

def main():
    town1 = graph('data/puertollano.graphml.xml')
    print(town1.belongNode('946409139')[0])
    town1.positionNode('982621804')
    town1.adjacentNode('956428288')

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("%s seconds" % (time.time() - start_time))