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
        tn2 = treeNode(p._init_state, 1, "", 1)
        tn3 = treeNode(p._init_state, 2, "", 2)
        f = frontier()
        f.insert(tn1)
        f.insert(tn2)
        f.insert(tn3)
        print(str(p._init_state))
        print(f._frontier)
        f.remove()
        print(f._frontier)
        print(p._init_state.createCode())
        print(p._state_space.successors(p._init_state))

    except ValueError:
        print("Error. Not a valid input")

if __name__ == '__main__':
    main()
