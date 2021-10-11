from node import Node
from transition import Transition

class Model():
    #defines required variables with no initial value
    def __init__(self):
        self.begin_state          #begins the process
        self.end_state            #ends the process

        self.valid_graph = False  #unverified graph is set to false
        self.nodes = []
        self.transitions = []     #Unordered transition

    def set_valid_graph(self):
        self.valid_graph = True

    def set_begin_state(self, node):
        self.begin_state = node
    
    def set_end_state(self, node):
        self.end_state = node

    def get_begin(self):
        return self.begin_state

    def get_end(self):
        return self.end_state

    def set_nodes(self, nodes):
        self.nodes = nodes

    def set_transitions(self, transitions):
        self.transitions = transitions

    def get_node_by_index(self, index):
        if (len(self.nodes) == 0):
            print("Getting node by index failed, empty list")
            return
        elif (len(self.nodes) < index):
            print("Getting node by index failed, index out of bounds")
            return
        return self.nodes[index]

    def get_transition_by_index(self, index):
        if (len(self.transitions) == 0):
            print("Getting transition by index failed, empty list")
            return
        elif (len(self.transitions) < index):
            print("Getting transition by index failed, index out of bounds")
            return
        return self.transitions[index]

    def get_number_of_nodes(self):
        return len(self.nodes)

    def get_number_of_transition(self):
        return len(self.transitions)