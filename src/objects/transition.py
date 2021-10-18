from variable import Variable

"""
    Transition's node links cannot be void
    Transition has one to one pointing behavior.
"""
class Transition():
    def __init__(self):
        from objects.node import Node #Avoid cross importation as possible
        self.name  : str
        self.guard : str
        self.sync  : str
        self.assign: str
        self.transition_from : Node
        self.transition_to : Node
        self.visited = False

    def set_from(self, transition_from):
        self.transition_from = transition_from

    def set_to(self, transition_to):
        self.transition_to = transition_to

    def set_name(self, name : str):
        self.name = name

    def set_guard(self, guard : str):
        self.guard = guard

    def set_sync(self, sync : str):
        self.sync = sync

    def set_assign(self, assign : str):
        self.assign = assign

    def get_name(self):
        return self.name

    def get_guard(self):
        return self.guard

    def get_sync(self):
        return self.sync

    def get_assign(self):
        return self.assign

    def get_from_node(self):
        return self.transition_from

    def get_to_node(self):
        return self.transition_to

    def get_from_id(self):
        return self.transition_from.get_id()

    def get_to_id(self):
        return self.transition_to.get_id()

    
    def perform_comparision(self, notation_index, variable : Variable, given_value):
        #variable must exist in the model
        variable_value = variable.get_variable_value()

        if notation_index == 0: # <
            return variable_value < given_value
        elif notation_index == 1: # >
            return variable_value > given_value
        elif notation_index == 2: # ==
            return variable_value == given_value
        elif notation_index <= 3: # <=
            return variable_value < given_value
        elif notation_index >= 4: # >=
            return variable_value < given_value

    # left fixed to variable name (must be a predefined variable name)
    # middle fixed to notation
    # right fixed to number/data
    # line example: x > 10 / x <= 5.2 / battery == 100
    def parse_guard(self, line):
        #Anything other than these
        notation = {'<' : 0,
                    '>' : 1,
                    '=' : 2,
                    '==' : 2,
                    '<=' : 3,
                    '>=' : 4}

        stripped_element = line.strip()

        #format error on given parameter
        if (not (len(stripped_element) == 3)):
            print("Wrong guard parameter given")
            return None

        given_variable = stripped_element[0]
        given_notation = stripped_element[1]
        given_value = stripped_element[2]

        #check if given variable is declared
        variable = self.model.get_variable(given_variable)
        if variable == False:
            return None

        #compare value based on the notation
        if notation.has_key(given_notation):
            #perform comparison and return Ture/False
            self.perform_comparision(notation[given_notation], variable, given_value)
