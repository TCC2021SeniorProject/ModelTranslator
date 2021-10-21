from objects.node import Node
from objects.transition import Transition
from objects.variable import Variable

class Model():
    START_STATE_TEXT = "START"
    END_STATE_TEXT = "END"

    #defines required variables with no initial value
    def __init__(self):
        self.start_state : Node   #starts the process
        self.end_state : Node     #ends the process

        self.valid_graph = False  #unverified graph is set to false
        self.nodes = []
        self.transitions = []     #Unordered transition
        self.variables = []       #conditional variables

    def set_valid_graph(self):
        self.valid_graph = True

    def is_valid_graph(self):
        return self.valid_graph

    def set_start_state(self, node):
        self.start_state = node
    
    def set_end_state(self, node):
        self.end_state = node

    #for non-predetermined variables(assignment/sync function)
    def update_variable(self, name, value):
        #No existing element
        index = self.get_variable_index(name)
        if (index == False):
            self.set_variable(name, value)
        else:
            new_variable = Variable()
            new_variable.set_variable_name(name)
            new_variable.set_variable_value(value)
            self.variables[index] = new_variable

    def set_variable(self, variable : Variable):
        self.variables.append(variable)

    def set_variable(self, name, value):
        new_variable = Variable()
        new_variable.set_variable_name(name)
        new_variable.set_variable_value(value)
        self.variables.append(new_variable)

    def get_variable(self, name):
        if (len(self.variables) == 0):
            return None
        else:
            for variable in self.variables:
                variable : Variable
                if (variable.get_variable_name() == name):
                    return variable
            return None

    def get_variables(self):
        return self.variables

    def get_variable_index(self, name):
        if (len(self.variables) == 0):
            return False
        else:
            for index, variable in enumerate(self.variables):
                variable : Variable
                if (variable.get_variable_name() == name):
                    return index
            return False

    def get_start(self):
        return self.start_state

    def get_end(self):
        return self.end_state

    def add_node(self, node):
        self.nodes.append(node)

    def set_nodes(self, nodes):
        self.nodes = nodes

    def get_nodes(self):
        return self.nodes

    def set_transitions(self, transitions : Transition):
        self.transitions = transitions

    def get_node_by_id(self, id):
        if (len(self.nodes) == 0):
            print("Getting node by index failed, empty list")
            return
        node : Node
        for node in self.nodes:
            if (node.get_id() == id):
                return node
        print("No node matching to the given id")
        return None

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

    #will return True if start state exists
    def find_start(self):
        if self.start_state == None:
            return False
        else:
            return True

    #will return True if end state exists
    def find_end(self):
        if self.end_state == None:
            return False
        else:
            return True

    def reset_visit(self):
        for node in self.nodes:
            node : Node
            node.set_unvisited()