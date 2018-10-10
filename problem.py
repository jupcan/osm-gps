from state import state
from stateSpace import stateSpace
import json

class problem():
    _path = ""
    _file = {}

    _state_space = stateSpace("","")
    _init_state = state("","","")

    def __init__(self, path):
        self._path = path
        self._file = self._readJson()

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
        json.printing()
    except ValueError:
        print("Error. Not a valid input")

if __name__ == '__main__':
    main()
