from state import state
from stateSpace import stateSpace
from treeNode import treeNode
import itertools
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
        """
        :return: json data from file
        """
        with open('json/' + self._json) as json_data:
            return json.load(json_data)

    def isGoal(self, state):
        """
        :param state: state class object
        :return: true/false if its list of nodes is empty
        """
        if bool(state._nodes): return False
        else: return True

    def distance(self, node1, node2):
        """
        :param node1: osm node id string
        :param node2: osm node id string
        :return: distance (meters) between node1 and node2
        """
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

    def createTreeNodes(self, ls, node, depthl, strategy, heu):
        """
        :param ls: list successors for a given state
        :param node: actual node string
        :param depthl: depth limit int
        :param strategy: strategy int
        :param heu: heuristic string
        :return: list of all problem's nodes
        """
        nodes = []; h = 0
        if(depthl >= node._d):
            for (action, result, cost) in ls:
                if result._nodes:
                    dmin = min([self.distance(result._current, n) for n in result._nodes])
                    if heu == 'h1':
                        h = dmin
                    elif heu == 'h0':
                        for a, b in itertools.combinations(result._nodes, 2):
                            h = dmin+min([self.distance(a, b)])
                s = treeNode(result, strategy, node, float(cost), action, h)
                nodes.append(s)
        return nodes
