from state import state
from stateSpace import stateSpace
from treeNode import treeNode
import json
import math
import hashlib

class problem():
    def __init__(self, json):
        self._json = json
        self._file = self._readJson()
        self._init_state = state(self._file["IntSt"]["node"], self._file["IntSt"]["listNodes"], self._file["IntSt"]["id"])
        xml = "/".join(self._file["graphlmfile"].strip("/").split('/')[1:]) + ".xml" #not getting town folder and adding .xml
        self._state_space = stateSpace(xml)
        self._visitedList = {}

    def _readJson(self):
        with open('json/' + self._json) as json_data:
            return json.load(json_data)

    def isGoal(self, state):
        #input: state, output: true/false if list of nodes is empty
        if bool(state._nodes): #true if has items, false otherwise
            return False
        else:
            return True

    def distance(self, node1, node2):
        (lng1, lat1) = self._state_space.positionNode(node1)
        (lng2, lat2) = self._state_space.positionNode(node2)
        earth_radius = 6371009

        phi1 = math.radians(float(lat1)); phi2 = math.radians(float(lat2))
        theta1 = math.radians(float(lng1)); theta2 = math.radians(float(lng2))
        d_phi = phi2 - phi1; d_theta = theta2 - theta1
        h = math.sin(d_phi/2)**2+math.cos(phi1)*math.cos(phi2)*math.sin(d_theta/2)**2
        h = min(1.0, h) #protect against floating point errors
        arc = 2*math.asin(math.sqrt(h))

        #return distance in units of earth_radius
        dist = arc*earth_radius
        return dist

    def createTreeNodes(self, ls, node, depthl, strategy):
        nodes = []
        heu = min([self.distance(self._init_state._current, n) for n in self._init_state._nodes])
        if(depthl >= node._d):
            for (action, result, cost) in ls:
                s = treeNode(result, strategy, node, float(cost), action, heu)
                nodes.append(s)
        return nodes
