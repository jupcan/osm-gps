from state import state
from stateSpace import stateSpace
from treeNode import treeNode
import json
import hashlib

class problem():
    _file = {}
    _init_state = state
    _state_space = stateSpace
    def __init__(self, json, strategy, depthl):
        self._json = json
        self._file = self._readJson()
        self._init_state = state(self._file["IntSt"]["node"], self._file["IntSt"]["listNodes"], self._file["IntSt"]["id"])
        xml = "/".join(self._file["graphlmfile"].strip("/").split('/')[1:]) + ".xml" #not getting town folder and adding .xml
        self._state_space = stateSpace(xml)
        self._strategy = strategy
        self._depthl = depthl

    def _readJson(self):
        with open(self._json) as json_data:
            return json.load(json_data)

    def createTreeNodes(self, node):
        childs = []
        states = self._state_space.successors(node._state)
        for (i, j, k) in states:
            aux = treeNode(j, self._strategy, node)
            if not self.checkVisited(aux._state):
                if(self._strategy == 2 or self._strategy == 3 and aux._d >= self._depthl): pass
            else: childs.append(aux)
        return childs

    def checkVisited(self, id):
        visited = False
        visited_states = self._state_space._visitedList
        for data in visited_states:
            aux = data
            if(self._state_space.equals(id, aux) and id._current._f > aux._current._f): visited = True
        return visited

    def isGoal(self, state):
        #input: state, output: true/false if list of nodes is empty
        if bool(state._nodes): #true if has items, false otherwise
            return False
        else:
            return True
