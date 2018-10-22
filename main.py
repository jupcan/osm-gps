#!/usr/bin/python3
# -*- coding: utf-8 -*-
from problem import problem
from frontier import frontier
from state import state
from treeNode import treeNode
import time

"""def stressTest(f, p):
        elements = 0
        while True:
            try:
                node = treeNode(p._init_state, 0, "", 0)
                f.insert(node)
                elements+=1
            except MemoryError:
                print('full memory')
                break
        return element"""

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
        print(p._init_state._md5)
        print(p._state_space._path)
        p._state_space.positionNode(p._init_state)
        print(p._state_space.belongNode(p._init_state))

        """print('elements until MemoryError: ')
        start = time.time()
        print(stressTest(f,p))
        print('time: %.11f' % (time.time() - start))"""

    except ValueError:
        print("Error. Not a valid input")

if __name__ == '__main__':
    main()
