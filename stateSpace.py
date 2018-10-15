from state import state

class stateSpace():

    _path = ""
    _states = {}
    
    def __init__(self, path, states):
        self._path = path
        self._states = states

    def Successors(self, state):
        """return [(acc1,NewState1,costAct1), ... , (accM,NewStateM,costActM)]
        where:
        - acci is a string like: "Origin ID: *** - Destination ID: ***"
        - NewStatei is the successor from state
        - costActi is the distance between state and NewStatei
        """
        acc = {}
        costAct = {}
        
        return acc, costAct

    def BelongNode(self, state):
        #output: True (if it belongs to the State Space) or False(in other case)
        if state in self._states:
            return True
        else:
            return False
