#!/usr/bin/python3
# -*- coding: utf-8 -*-
from graph import graph

def main():
    town1 = graph('data/navalpino.graphml.xml')
    print(town1.belongNode('5071906333')[0])
    town1.positionNode('5071906333')

if __name__ == '__main__':
    main()