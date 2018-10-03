#!/usr/bin/python3
# -*- coding: utf-8 -*-
from graph import graph
import time

def main():
    town1 = graph('data/anchuras.graphml.xml')
    start_time = time.time()
    print(town1.belongNode('4331489627'))
    print("%s seconds" % (time.time() - start_time))
    town1.positionNode('4331489627')
    town1.adjacentNode('4331489627')

if __name__ == '__main__':
    main()