from state import state
from stateSpace import stateSpace
import json
import hashlib

class problem():
    _file = {}
    _init_state = state("", "", "")
    _state_space = stateSpace("")
    def __init__(self, path):
        self._path = path
        self._file = self._readJson()
        self._init_state = state(self._file["IntSt"]["node"], self._file["IntSt"]["listNodes"], self._file["IntSt"]["id"])
        self._state_space = stateSpace(self._file["graphlmfile"])

    def _readJson(self):
        with open(self._path) as json_data:
            return json.load(json_data)

    def isGoal(self, state):
        #input: initial state, output: true/false if list of nodes is empty
        if bool(state.getNodes()): #bool(<dictionary>) -> true if has items, false otherwise
            return False
        else:
            return True
