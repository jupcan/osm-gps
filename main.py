#!/usr/bin/python3
# -*- coding: utf-8 -*-

from problem import problem
from frontier import frontier
from state import state
from treeNode import treeNode

def main():
    try:
        filename = input('json file: ')
        if filename.isdigit():
            raise ValueError
        p = problem('%s.json' % filename)
        tn1 = treeNode(p._init_state, 0, "", 0)
        print(str(p._init_state))
        print(p._init_state._md5)
    except ValueError:
        print("Error. Not a valid input")

if __name__ == '__main__':
    main()
