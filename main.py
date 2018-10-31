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
        tn1 = treeNode(p._init_state, 0, "", 0)
        tn2 = treeNode(p._init_state, 1, "", 1)
        tn3 = treeNode(p._init_state, 2, "", 2)
        f = frontier()
        f.insert(tn1)
        f.insert(tn2)
        f.insert(tn3)
        #print(str(p._init_state))
        print(p._state_space._path)
        f.remove()
        print(p._state_space.successors(p._init_state))

    except ValueError:
        print("Error. Not a valid input.")

def limsearch(self, problem, strategy, depthl):
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
    if(sol): return createSol(act);
    else: return None

def search(self, problem, strategy, depthl, depthi):
    depthact = depthi
    sol = None
    while(not sol and depthact <= depthl):
        sol = limsearch(problem, strategy, depthact)
        depthact += depthi
    return sol

if __name__ == '__main__':
    main()
