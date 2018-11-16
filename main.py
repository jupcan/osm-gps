#!/usr/bin/python3
#-*- coding: utf-8 -*-
from pprint import pprint, pformat
from problem import problem
from frontier import frontier
from treeNode import treeNode
from state import state
from yattag import Doc
import time
import sys

def main():
    filename, strategy, depthl, pruning = askInfo()
    if(strategy == 3): depthi = int(input('depth increment: '))

    p = problem('%s.json' % filename)
    print(p._state_space._path.lower())

    itime = time.time()
    #run algorithms
    if(strategy == 3): sol = search(p, strategy, depthl, depthi, pruning)
    else: sol, num_f = limSearch(p, strategy, depthl, pruning)
    etime = time.time()
    createSolution(sol, itime, etime, num_f)

def askInfo():
    try:
        filename = input('json file: ')
        if filename.isdigit():
            raise ValueError
        print(filename + ".json") #print json file name
        switch = {
        0: 'breath-first search', 1: 'depth-first search', 2: 'depth-limited search',\
        3: 'iterative deepening search', 4: 'uniform cost search', 5: 'greedy search', 6: 'a* search'}
        print("\n".join("{}: {}".format(k, v) for k, v in switch.items()))

        strategy = int(input('strategy: '))
        if isinstance(strategy, str) or strategy > 6 or strategy < 0: raise ValueError

        yes = {'y','yes','yay'}; no = {'n','no','nay'}
        pruning = input('pruning(y/n): ').lower()
        if pruning in yes: pruning = True; print(switch[strategy] + ' w/ pruning')
        elif pruning in no: pruning = False; print(switch[strategy] + ' w/o pruning')
        else: raise ValueError

        depthl = int(input('depth: '))-1
        if isinstance(depthl, str): raise ValueError
        return filename, strategy, depthl, pruning
    except ValueError:
        print("Error. Not a valid input.")
        sys.exit(1)

def limSearch(problem, strategy, depthl, pruning):
    f = frontier()
    num_f = 0
    initial = treeNode(problem._init_state, strategy)
    f.insert(initial); num_f += 1
    problem._visitedList[initial._state._md5] = initial._f
    sol = False
    while(not sol and not f.isEmpty()):
        act = f.remove()
        if(problem.isGoal(act._state)): sol = True
        else:
            ls = problem._state_space.successors(act._state)
            ln = problem.createTreeNodes(ls, act, depthl, strategy)
            if pruning:
                for node in ln:
                    if node._state._md5 not in problem._visitedList:
                        f.insert(node); num_f += 1
                        problem._visitedList[node._state._md5] = node._f
                    elif abs(node._f) < abs(problem._visitedList[node._state._md5]):
                        f.insert(node); num_f += 1
                        problem._visitedList[node._state._md5] = node._f
            else:
                for node in ln: f.insert(node)
    if(sol): return act, num_f
    else: return None

def search(problem, strategy, depthl, depthi, pruning):
    depthact = depthi
    sol = None
    while(not sol and depthact <= depthl+1):
        print(depthact)
        sol = limSearch(problem, strategy, depthact, pruning)
        print(sol)
        depthact += depthi
    return sol

def createSolution(sol, itime, etime, num_f):
    if(sol is not None):
        list = []
        act = sol
        list.append(act._action)
        while(act._parent is not None and act._parent._action is not None):
            list.append(act._parent._action)
            act = act._parent
        list.reverse()
        print('cost: %.3f, depth: %d, spatialcxty: %d, temporalcxty: %fs\ncheck out.txt for more info' % (sol._cost, sol._d, num_f, etime-itime))
        writeSolution(sol, itime, etime, num_f, list)
        createGpx(list)
    else:
        print('no solution found for the given depth limit')

def writeSolution(sol, itime, etime, num_f, list):
    txt = open('out.txt','w')
    if(sol is not None):
        line1 = 'cost: %.3f, depth: %d, spatialcxty: %d, temporalcxty: %fs\n' % (sol._cost, sol._d, num_f, etime-itime)
        line2 = 'goal node: %s\n' % str(sol)
        line3 = time.strftime('time and date: %H:%M:%S-%d/%m/%Y\n\n')
        line4 = pformat(list)
        txt.writelines([line1, line2, line3, line4])
    else:
        txt.write('no solution found for the given depth limit')
    txt.close()

def createGpx(list):
    gpx = open('out.gpx','w')
    doc, tag, text = Doc().tagtext()
    doc.asis('<?xml version="1.0" encoding="UTF-8"?>\n')

    with tag('gpx', version='1.0'):
        with tag('trk'):
            with tag('name'):
                text('solgpx')
            with tag('trkseg'):
                for n in list:
                    with tag('trkpt', lat='39.4026419', lon='-3.1254799'): text('')
    gpx.write(doc.getvalue())

if __name__ == '__main__':
    main()
