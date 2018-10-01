#!/usr/bin/python3
# -*- coding: utf-8 -*-
from graph import graph

def main():
    town1 = graph('data/anchuras.graphml.xml')
    print(town1.belongNode('946409139')[0])
    town1.positionNode('982621804')
    town1.adjacentNode('4331489709')

if __name__ == '__main__':
    main()