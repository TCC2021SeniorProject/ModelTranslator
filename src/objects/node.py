from typing import List

from objects.transition import Transition
from objects.variable import Variable

"""
    Node consists of following elements

    name          : String value used as function name
    id            : Unique identification name
    commit        : ?
    parameters(s) : parameters
    transition(s) : One direction node pointer linkage

    @TODO: Implement commit, parameter section

    @AUTHOR: Marco-Backman
"""

class Node():
    def __init__(self, id : str, name : str):
        self.id : str = id
        self.name : str = name
        #Not implemented yet
        self.commit : str
        self.is_commit = False
        self.visited = False
        #Not implemented yet.
        self.parameter_list : List[Variable] = []
        self.transition_list : List[Transition] = []
        print(name + "Node created")

    def get_id(self) -> str:
        return self.id

    def set_id(self, id : str):
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name : str):
        self.name = name

    def get_transitions(self) -> List[Transition]:
        return self.transition_list

    def add_transition(self, transition : Transition):
        self.transition_list.append(transition)
        print("Transition added")

    def transition_count(self) -> int:
        return len(self.transition_list)

    def is_visited(self) -> bool:
        return self.visited

    def set_visited(self) -> bool:
        self.visited = True

    def set_unvisited(self) -> bool:
        self.visited = False
    
    #Not implemented yet
    def get_commit(self):
        return self.commit

    #Not implmeneted yet
    def set_commit(self, commit : str):
        self.is_commit = True
        self.commit = commit