#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pprint import pprint, pformat
from problem import problem
from frontier import frontier
from treeNode import treeNode
from state import state
import time
import sys

def main():
    filename, strategy = askInfo()
    depthl = int(input('depth: '))-1
    if(strategy == 3): depthi = int(input('depth increment: '))
    p = problem('%s.json' % filename, strategy, depthl)
    print(p._state_space._path.lower())
    itime = time.time()
    #run algorithms
    if(strategy == 3): sol = search(p, strategy, depthl, depthi)
    else: sol = limSearch(p, strategy, depthl)
    etime = time.time()
    createSol(sol, itime, etime)

def askInfo():
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
    initial = treeNode(problem._init_state, strategy)
    f.insert(initial)
    sol = False

    while(not sol and not f.isEmpty()):
        act = f.remove()
        if(problem.isGoal(act._state)): sol = True
        else:
            ls = problem._state_space.successors(act._state)
            ln = createTreeNodes(ls, act, depthl, strategy)
            for node in ln: f.insert(node)
    if(sol): return act
    else: return None

def search(problem, strategy, depthl, depthi):
    depthact = depthi
    sol = None
    while(not sol and depthact <= depthl):
        sol = limSearch(problem, strategy, depthact)
        depthact += depthi
    return sol

def createTreeNodes(ls, node, depthl, strategy):
    tree = []
    if(depthl >= node._d):
        for (action, result, cost) in ls:
            s = treeNode(result, strategy, node, float(cost), action)
            tree.append(s)
    return tree

def createSol(sol, itime, etime):
    if(sol is not None):
        list = []
        act = sol
        list.append(act._action)
        while(act._parent is not None and act._parent._action is not None):
            list.append(act._parent._action)
            act = act._parent
        list.reverse()
        print('cost: %f, depth: %d, elapsed time: %fs\ncheck out.txt for more info' % (sol._cost, sol._d, etime-itime))
        pprint(list)
        writeSol(sol, itime, etime, list)
    else:
        print('no solution found for the given depth limit')

def writeSol(sol, itime, etime, list):
    txt = open('out.txt','w')
    if(sol is not None):
        line1 = 'cost: %f, depth: %d, elapsed time: %fs\n' % (sol._cost, sol._d, etime-itime)
        line2 = 'goal node: %s\n' % str(sol)
        line3 = time.strftime('time and date: %H:%M:%S-%d/%m/%Y\n\n')
        line4 = pformat(list)
        txt.writelines([line1, line2, line3, line4])
    else:
        txt.write('no solution found for the given depth limit')
    txt.close()

if __name__ == '__main__':
    main()
