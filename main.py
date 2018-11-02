#!/usr/bin/python3
# -*- coding: utf-8 -*-
from problem import problem
from frontier import frontier
from state import state
from treeNode import treeNode
import time
import sys
from pprint import pprint

def main():
    filename, strategy = askinfo()
    depthl = 100000
    if(strategy == 2): depthl = int(input('depth: '))
    if(strategy == 3): depthi = int(input('depth increment: '))
    p = problem('%s.json' % filename, strategy, depthl)
    print(p._state_space._path.lower())
    itime = time.time()
    #run algorithms
    if(strategy == 3): sol = search(p, strategy, depthl, depthi)
    else: sol = limSearch(p, strategy, depthl)
    etime = time.time()
    createSol(sol, itime, etime)

def askinfo():
    try:
        filename = input('json file: ')
        if filename.isdigit():
            raise ValueError
        print(filename + ".json") #print json file name
        switch = {
        0: 'breath-first search', 1: 'depth-first search', 2: 'depth-limited search',\
        3: 'iterative deepening search', 4: 'uniform cost search', 5: 'a* search'}
        print("\n".join("{}: {}".format(k, v) for k, v in switch.items()))
        strategy = int(input('strategy: '))
        if isinstance(strategy, str) or strategy > 5 or strategy < 0:
            raise ValueError
        print(switch[strategy])
        return filename, strategy
    except ValueError:
        print("Error. Not a valid input.")
        sys.exit(1)

def limSearch(problem, strategy, depthl):
    f = frontier()
    initial = treeNode(problem._init_state, problem._strategy)
    f.insert(initial)
    sol = False

    while(not sol and not f.isEmpty()):
        act = f.remove()
        problem._state_space.visitedList(act[1]._state)
        if(problem.isGoal(act[1]._state)): sol = True
        else:
            for data in problem.createTreeNodes(act[1]): f.insert(data)
        print(f._frontier)
    if(sol): return act
    else: return None

def search(problem, strategy, depthl, depthi):
    depthact = depthi
    sol = None
    while(not sol and depthact <= depthl):
        sol = limSearch(problem, strategy, depthact)
        depthact += depthi
    return sol

def createSol(sol, itime, etime):
    if(sol is not None):
        print('cost: %d, depth: %d, elapsed time: %fms\ncheck out.txt for more info' % (sol[1]._cost, sol[1]._d, etime-itime))
        txt = open('out.txt','w')
        txt.write('cost: %d, depth: %d, elapsed time: %fms' % (sol[1]._cost, sol[1]._d, etime-itime))
    else:
        print('no solution found for the given depth limit')

if __name__ == '__main__':
    main()
