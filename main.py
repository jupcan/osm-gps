#!/usr/bin/python3
# -*- coding: utf-8 -*-
from graph import graph
import time

def main():
    town1 = graph('data/puertollano.graphml.xml')
    start_time = time.time()
    print(town1.belongNode('956428288')[0])
    print("%s seconds" % (time.time() - start_time))
    #town1.positionNode('982621804')
    #town1.adjacentNode('253849830')

if __name__ == '__main__':
    main()