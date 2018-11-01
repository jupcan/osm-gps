#!/usr/bin/python3
# -*- coding: utf-8 -*-
from problem import problem
from frontier import frontier
from state import state
from treeNode import treeNode
import time
import sys

def main():
    filename, strategy = askinfo()
    depthl = 999
    if(strategy == 2): depthl = int(input('depth: '))
    if(strategy == 3): depthi = int(input('depth increment: '))
    p = problem('%s.json' % filename, strategy, depthl)
    print(p._state_space._path.lower())
    itime = time.time()
    #run algorithms
    if(strategy == 3): sol = search(p, strategy, depthl, depthi)
    else: sol = limsearch(p, strategy, depthl)
    etime = time.time()
    createsol(sol, itime, etime)
    #print(p._state_space.successors(p._init_state))

def askinfo():
    try:
        filename = input('json file: ')
        if filename.isdigit():
            raise ValueError
        print(filename + ".json") #print json file name
        strategy = int(input('strategy: '))
        if isinstance(strategy, str) or strategy > 5 or strategy < 0:
            raise ValueError
        switch = {
            0: 'breath-first search', 1: 'depth-first search', 2: 'depth-limited search',\
            3: 'iterative deepening search', 4: 'uniform cost search', 5: 'a* search'}
        print(switch[strategy])
        return filename, strategy
    except ValueError:
        print("Error. Not a valid input.")
        sys.exit(1)

def limsearch(problem, strategy, depthl):
    f = frontier()
    initial = treeNode(problem._init_state)
    f.insert(initial)
    sol = False

    while(not sol and not f.isEmpty()):
        act = f.remove()
        if(problem.isGoal(act._state)):
            sol = True
        else:
            ls = problem._state_space.successors(act._state)
            ln = createTreeNodes(ls, act, depthl, strategy)
            f.insert(ln)
    if(sol): return createsol(act)
    else: return None

def search(problem, strategy, depthl, depthi):
    depthact = depthi
    sol = None
    while(not sol and depthact <= depthl):
        sol = limsearch(problem, strategy, depthact)
        depthact += depthi
    return sol

def createsol(sol, itime, etime):
    if(sol is not None):
        print('cost: %d\ndepth: %d\nelapsed time: %dms\ncheck out.txt for more info' % (sol._cost, sol._d, itime-etime))
        writesol(sol)
    else:
        print('no solution found for the given depth limit')

if __name__ == '__main__':
    main()
