#!/usr/bin/python3
# -*- coding: utf-8 -*-
from problem import problem
from frontier import frontier
from state import state
from treeNode import treeNode
from collections import OrderedDict

def main():
    try:
        filename = input('json file: ')
        if filename.isdigit():
            raise ValueError
        p = problem('%s.json' % filename)
        tn1 = treeNode(p._init_state, 0, "", 0)
        tn2 = treeNode(p._init_state, 1, "", 1)
        f = frontier()
        print(str(p._init_state))
        print(tn1._f)
        print(p._init_state._md5)
        f.insert(tn1)
        f.insert(tn2)
        print(str(f))
    except ValueError:
        print("Error. Not a valid input")

if __name__ == '__main__':
    main()
