#!/usr/bin/python3
# -*- coding: utf-8 -*-
from problem import problem
from frontier import frontier
from state import state
from treeNode import treeNode
import time
import sys

def stressTest(f,p):
    elements = 0
    avg = 0
    maxim = 0
    minim = 9999
    
    try:
        while True:
            try:
                newState = state(str(int(p._init_state._current)+elements), p._init_state._nodes)
                if(elements == 0):
                    node = treeNode(p._init_state, 0, "", elements)
                else:
                    node = treeNode(newState, 0, "", elements)

                start = time.time()
                f.insert(node)
                end = time.time()

                timer = end - start
                avg += timer
                if(timer > maxim):
                    maxim = timer
                if(timer < minim):
                    minim = timer
                
                elements+=1
                
            except MemoryError:
                print("full memory")
                print('nº elements: '+elements)
                print('min time: %.11f' % minim)
                print('max time: %.11f' %  maxim)
                print('avg time: %.11f' % (avg/elements))
                break
    except KeyboardInterrupt:
            print('min time: %.11f' % minim)
            print('max time: %.11f' %  maxim)
            print('avg time: %.11f' % (avg/elements))
            return elements
    return elements

def main():
    try:
        filename = input('json file: ')
        if filename.isdigit():
            raise ValueError
        print(filename + ".json") #print json file name
        p = problem('%s.json' % filename)
        f = frontier()
        
        """tn1 = treeNode(p._init_state, 0, "", 0)
        tn2 = treeNode(p._init_state, 1, "", 1)
        tn3 = treeNode(p._init_state, 2, "", 2)

        
        f.insert(tn1)
        f.insert(tn2)
        f.insert(tn3)

        #print(str(p._init_state))

        "while not f._frontier.empty():
            print(f._frontier.get())"""

        #f.remove()
        #print(f._frontier)
        #print(p._init_state._md5)
        #print(p._state_space._path)
        #print(p._state_space.belongNode(p._init_state))
        #p._state_space.successors(p._init_state)
        #print(p.isGoal(p._init_state))

        print('elements until memory error: ')
        start = time.time()
        print(stressTest(f,p))
        print('time: %.11f' % (time.time() - start))
        #print(f._frontier[min(f._frontier)])

    except ValueError:
        print("Error. Not a valid input")
            
if __name__ == '__main__':
    main()
