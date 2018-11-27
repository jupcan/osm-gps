#!/usr/bin/python3
#-*- coding: utf-8 -*-
from pprint import pprint, pformat
from problem import problem
from frontier import frontier
from treeNode import treeNode
from subprocess import call
from state import state
from lxml import etree
import time, sys, gc, os

def main():
    filename, strategy, depthl, pruning, stat = askInfo()
    if(strategy == 3): depthi = int(input('depth increment: '))

    p = problem('%s.json' % filename)
    print(p._state_space._path.lower())

    itime = time.time()
    #run algorithms
    if(strategy == 3): sol = search(p, strategy, depthl, depthi, pruning)
    else: sol, num_f = limSearch(p, strategy, depthl, pruning)
    etime = time.time()
    createSolution(sol, itime, etime, num_f)
    createGpx(p, sol, itime, etime, num_f, stat)
    call(['solu/gpx2svg', '-i', 'solu/out.gpx', '-o', 'solu/out.svg'])

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
        if pruning in yes: pruning = True; stat = switch[strategy] + ' w/ pruning'; print(stat)
        elif pruning in no: pruning = False; stat = switch[strategy] + ' w/o pruning'; print(stat)
        else: raise ValueError

        depthl = int(input('depth: '))-1
        if isinstance(depthl, str): raise ValueError
        return filename, strategy, depthl, pruning, stat
    except ValueError:
        print("error. not a valid input")
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
                for node in ln: f.insert(node); num_f += 1
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
    txt = open('solu/out.txt','w')
    if(sol is not None):
        list = []
        act = sol
        list.append(act._action)
        while(act._parent is not None and act._parent._action is not None):
            list.append(act._parent._action)
            act = act._parent
        list.reverse()
        print('cost: %.3f, depth: %d, spatialcxty: %d, temporalcxty: %fs\ncheck out.txt for more info' % (sol._cost, sol._d, num_f, etime-itime))
        line1 = 'cost: %.3f, depth: %d, spatialcxty: %d, temporalcxty: %fs\n' % (sol._cost, sol._d, num_f, etime-itime)
        line2 = 'goal node: %s - %s\n' % (sol, sol._state._current)
        line3 = time.strftime('time and date: %H:%M:%S-%d/%m/%Y\n\n')
        line4 = pformat(list)
        txt.writelines([line1, line2, line3, line4])
    else:
        print('no solution found for the given depth limit')
        txt.write('no solution found for the given depth limit')
    txt.close()

def createGpx(problem, sol, itime, etime, num_f, stat):
    if(sol is not None):
        list, points = [], []
        act = sol
        list.append(problem._state_space.positionNode(act._state._current))
        while(act._parent is not None):
            list.append(problem._state_space.positionNode(act._parent._state._current))
            act = act._parent
        list.reverse()
        points.append(problem._init_state._current)
        for i in problem._init_state._nodes: points.append(i)

    gpx = open('solu/out.gpx','wb')
    root = etree.Element('gpx', version='1.0'); root.text = '\n'
    for n in points:
        wpt = etree.SubElement(root, 'wpt', lat=problem._state_space.positionNode(n)[0], lon=problem._state_space.positionNode(n)[1]); wpt.tail = '\n'
        w_name = etree.SubElement(wpt, 'name'); w_name.text = n
        w_desc = etree.SubElement(wpt, 'desc'); w_desc.text = problem._state_space.positionNode(n)[0] + ', ' + problem._state_space.positionNode(n)[1]
    trk = etree.SubElement(root, 'trk')
    t_name = etree.SubElement(trk, 'name'); t_name.text = 'out.gpx'; t_name.tail = '\n'
    desc = etree.SubElement(trk, 'desc'); desc.text = '%s, cost: %.3f, depth: %d, scxty: %d, tcxty: %fs' % (stat, sol._cost, sol._d, num_f, etime-itime); desc.tail = '\n'
    link = etree.SubElement(trk, 'link', href='http://www.uclm.es')
    text = link = etree.SubElement(link, 'text'); text.text = 'uclm project'
    trkseg = etree.SubElement(trk, 'trkseg'); trkseg.text = '\n'
    for n in list:
        trkpt = etree.SubElement(trkseg, 'trkpt', lat=n[0].zfill(10), lon=n[1].zfill(10)); trkpt.tail = '\n'
        date = etree.SubElement(trkpt, 'time'); date.text = time.strftime('%Y-%m-%dT%H:%M:%S')
    doc = etree.ElementTree(root)
    doc.write(gpx, xml_declaration=True, encoding='utf-8')
    gpx.close()

if __name__ == '__main__':
    main()
