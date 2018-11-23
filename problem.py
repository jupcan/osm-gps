from state import state
from stateSpace import stateSpace
from treeNode import treeNode
import json
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

    def createTreeNodes(self, ls, node, depthl, strategy):
        nodes = []
        if(depthl >= node._d):
            for (action, result, cost, heu) in ls:
                s = treeNode(result, strategy, node, float(cost), action, heu)
                nodes.append(s)
        return nodes
