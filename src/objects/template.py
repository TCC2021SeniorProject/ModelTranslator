from re import template
from typing import List

from objects.node import Node
from objects.transition import Transition

"""
    Stores each UPPAAL template into an object form.
    This will contain every information that a single template must possess.

    @TODO:

    @AUTHOR: Marco-Backman
"""

class Template:
    START_STATE_TEXT = "START"
    END_STATE_TEXT = "END"

    #defines required variables with no initial value
    def __init__(self):
        from objects.variable import Variable
        self.name = ""
        self.start_state : Node = None
        self.end_state : List[Node] = []
        self.nodes : List[Node] = []
        self.transitions : List[Transition] = []
        #unimplented
        self.variables : List[Variable] = []
        self.parameters : List[Variable] = []
        self.valid_graph = False

    def get_template_name(self):
        return self.name

    def set_template_name(self, name) -> str:
        if name == None:
            self.name = ""
        else:
            self.name = name

    def get_nodes(self) -> List[Node]:
        return self.nodes

    def get_node_by_id(self, id) -> Node:
        if (len(self.nodes) == 0):
            raise Exception("No node matching to the given id")
        node : Node
        for node in self.nodes:
            if (node.get_id() == id):
                return node
        raise Exception("No node matching to the given id")

    def add_node(self, node):
        self.nodes.append(node)

    def get_transition_num(self) -> int:
        return len(self.transitions)

    def set_transitions(self, transitions : List[Transition]):
        self.transitions = transitions

    def add_transitions(self, transition: Transition):
        self.transitions.append(transition)

    def is_valid_graph(self):
        return self.valid_graph

    def set_valid_graph(self):
        self.valid_graph = True

    def get_start(self) -> Node:
        return self.start_state

    def set_start(self, node):
        self.start_state = node

    def is_end(self, target_node : Node) -> bool:
        for node in self.end_state:
            node : Node
            if node.get_id == target_node.get_id:
                return True
        return False

    def get_end_list(self) -> List[Node]:
        if len(self.end_state) == 0:
            return None
        return self.end_state

    def add_end(self, node):
        #Check for duplication
        if self.is_end(node):
            return
        else:
            self.end_state.append(node)

    #Used for assign command from UPPAAL
    def update_variable(self, name, value):
        from objects.variable import Variable
        index = self.get_variable_index(name)
        new_variable = Variable()
        new_variable.set_variable_name(name)
        new_variable.set_variable_value(value)
        if (index == False):
            self.variables.append(new_variable)
        else:
            self.variables[index] = new_variable

    def get_parameters(self):
        return self.parameters

    def get_parameter(self, parameter_name):
        from objects.variable import Variable
        if (len(self.parameters) == 0):
            return None
        else:
            for parameter in self.parameters:
                parameter : str
                if (parameter == parameter_name):
                    return parameter
            return None

    def add_parameter(self, parameter : str):
        self.parameters.append(parameter)

    def set_parameters(self, parameters : List[str]):
        self.parameters = parameters

    def get_variable_index(self, name) -> int:
        from objects.variable import Variable
        if (len(self.variables) == 0):
            return False
        else:
            for index, variable in enumerate(self.variables):
                variable : Variable
                if (variable.get_variable_name() == name):
                    return index
            return False

    def add_variable(self, variable):
        print("Variable added")
        self.variables.append(variable)

    def set_variables(self, variables):
        self.variables = variables

    def get_node_size(self) -> int:
        return len(self.nodes)

    def get_transition_size(self) -> int:
        return len(self.transitions)

    def reset_visit(self):
        for node in self.nodes:
            node : Node
            node.set_unvisited()

    def print_info(self):
        #Template
        print("Template name: " + self.name)

        #Local var
        for variable in self.variables:
            variable.print_info()

        #Node
        for node in self.nodes:
            node.print_info()

        #Transitions
        for transition in self.transitions:
            transition.print_info()
