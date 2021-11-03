from objects.node import Node
from objects.transition import Transition
from objects.variable import Variable

class Model():
    START_STATE_TEXT = "START"
    END_STATE_TEXT = "END"

    #defines required variables with no initial value
    def __init__(self):
        self.name = ""
        self.start_state : Node = None
        self.end_state = []
        self.nodes = []
        self.transitions = []
        self.variables = []
        self.valid_graph = False

    def get_model_name(self):
        return self.name

    def get_nodes(self):
        return self.nodes

    def get_node_by_id(self, id):
        if (len(self.nodes) == 0):
            raise Exception("No node matching to the given id")
        node : Node
        for node in self.nodes:
            if (node.get_id() == id):
                return node
        raise Exception("No node matching to the given id")

    def add_node(self, node):
        print("Node added")
        self.nodes.append(node)

    def get_transition_num(self):
        return len(self.transitions)

    def set_transitions(self, transitions : Transition):
        self.transitions = transitions

    def is_valid_graph(self):
        return self.valid_graph

    def set_valid_graph(self):
        self.valid_graph = True

    def get_start(self):
        return self.start_state

    def set_start(self, node):
        self.start_state = node
    
    def is_end(self, target_node : Node):
        for node in self.end_state:
            node : Node
            if node.get_id == target_node.get_id:
                return True
        return False

    def get_end_list(self):
        if len(self.end_state) == 0:
            return None
        return self.end_state

    def add_end(self, node):
        #Check for duplication
        if self.is_end(node):
            return
        else:
            self.end_state.append(node)

    def set_model_name(self, name):
        if name == None:
            self.name = ""
        else:
            self.name = name

    #Used for assign command from UPPAAL
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

    def get_variables(self):
        return self.variables

    def get_variable(self, name):
        if (len(self.variables) == 0):
            return None
        else:
            for variable in self.variables:
                variable : Variable
                if (variable.get_variable_name() == name):
                    return variable
            return None

    def get_variable_index(self, name):
        if (len(self.variables) == 0):
            return False
        else:
            for index, variable in enumerate(self.variables):
                variable : Variable
                if (variable.get_variable_name() == name):
                    return index
            return False

    def set_variable(self, variable : Variable):
        self.variables.append(variable)

    def set_variables(self, variables):
        self.variables = variables

    def get_node_size(self):
        return len(self.nodes)

    def get_transition_size(self):
        return len(self.transitions)

    def reset_visit(self):
        for node in self.nodes:
            node : Node
            node.set_unvisited()