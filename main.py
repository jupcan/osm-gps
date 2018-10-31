#!/usr/bin/python3
# -*- coding: utf-8 -*-
from problem import problem
from frontier import frontier
from state import state
from treeNode import treeNode
import time
import sys

def main():
    try:
        filename = input('json file: ')
        if filename.isdigit():
            raise ValueError
        print(filename + ".json") #print json file name
        p = problem('%s.json' % filename)
        print(p._state_space._path)
        strategy = int(input('strategy: '))
        if isinstance(strategy, str) or strategy > 4 or strategy < 0:
            raise ValueError
        print(p._state_space.successors(p._init_state))

    except ValueError:
        print("Error. Not a valid input.")

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
    if(sol): return createsol(act);
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
