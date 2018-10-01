#!/usr/bin/python3
# -*- coding: utf-8 -*-
from graph import graph

def main():
    town1 = graph('data/navalpino.graphml.xml')
    print(town1.belongNode('950073331')[0])
    town1.positionNode('950073331')

if __name__ == '__main__':
    main()