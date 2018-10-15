from state import state as state
from stateSpace import stateSpace as stateSpace
import json

class problem(): 
    _path = ""
    _file = {}
<<<<<<< HEAD
    
=======

    _state_space = stateSpace("","")
    _init_state = state("","","")

>>>>>>> 9bd4128d85a0df2e3fa66c26636cfae94c42c2c7
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
        json = problem(filename)
        print(json._state_space.BelongNode(json._init_state))
    except ValueError:
        print("Error. Not a valid input")

if __name__ == '__main__':
    main()
