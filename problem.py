from state import state as state
from stateSpace import stateSpace as space
import json

class problem():
    _path = ""
    _file = {}
    
    def __init__(self, path):
        self._path = path
        self._file = self._readJson()

    def _readJson(self):
        with open(self._path) as json_data:
            d = json.load(json_data)

    def isGoal(state):
        """isGoal(state) => True or False
        A state satisfies this function if the list of nodes is empty
        """
        if bool(space.getStates()): #bool(<dictionary>) -> true if has items, false otherwise
            return False
        else:
            return True
    
