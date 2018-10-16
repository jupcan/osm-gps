from state import state as state
from stateSpace import stateSpace as stateSpace
import json
import hashlib

class problem(): 
    _path = ""
    _file = {}

    _state_space = stateSpace("","")
    _init_state = state("","","")

    def __init__(self, path):
        self._path = path
        self._file = self._readJson()
        self._init_state = state(self._file["IntSt"]["node"],self._file["IntSt"]["listNodes"],self._file["IntSt"]["id"])
        self._state_space = stateSpace(self._file["graphlmfile"], self._init_state)

    def _readJson(self):
        with open(self._path) as json_data:
            return json.load(json_data)

    def printing(self):
        print(self._file["IntSt"])

    def isGoal(self,state):
        """isGoal(state) => True or False
        A state satisfies this function if the list of nodes is empty
        """
        if bool(state.getNodes()): #bool(<dictionary>) -> true if has items, false otherwise
            return False
        else:
            return True
"""
Main for testing json reading
"""
def main():
    try:
        filename = 'example.json'
        if filename.isdigit():
            raise ValueError
        p = problem(filename)
        #cadena = p._file["IntSt"]["node"] + " : " + str(p._file["IntSt"]["listNodes"])
        print(p._init_state._md5)
    except ValueError:
        print("Error. Not a valid input")

if __name__ == '__main__':
    main()
