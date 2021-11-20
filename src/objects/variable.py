"""
    Stores various types of UPPAAL variables and values accordingly.
    Converts UPPAAL operator notations into Python operator notations.
    Assign default value of the varaible when UPPAAL has not given any.

    Implemented types:
        Boolean    - o
        integer    - o
        double     - o
        channel    - o
        clocks     - x
        scalar     - x
        array      - o
        structures - x
        constraints- x

    @TODO: 
        1. Implement channel
        2. Implement array
        3. Implement struct

    @AUTHOR: Marco-Backman
"""

class Variable:
    var_type_dic = {'int' : 0,
                'bool' : 1,
                'boolean' : 1,
                'float' : 2,
                'double' : 2,
                'channel' : 3,
                'chan' : 3,
                'array' : 4,
                'arr' : 4}

    def __init__(self, var_type, var_name, var_value):
        self.var_type = var_type.lower()
        self.var_name = var_name
        self.var_value = var_value
        var_type_index = self.var_type_dic.get(var_type)
        if var_value == "":
            self.set_defualt_value(var_type, var_type_index)
        else:
            if var_type_index == 1: #UPPAAL sets boolean value to 0, 1
                if var_value == "0" or var_value == "false":
                    self.var_value = "False"
                elif var_value == "1" or var_value == "true":
                    self.var_value = "True"

    def set_defualt_value(self, var_type, var_type_index):
        var_type = var_type.lower()
        if var_type_index == 0:
            self.var_value = 0
        elif var_type_index == 1:
            self.var_value = False
        elif var_type_index == 2:
            self.var_value = 0.0
        elif var_type_index == 3:
            self.var_value = "None"
        elif var_type_index == 4:
            self.var_value = "[]"
        else:
            print("Variable type error")

    def get_variable_type(self):
        return self.var_type

    def set_variable_type(self, type):
        self.var_type = type

    def get_variable_name(self):
        return self.var_name

    def set_variable_name(self, name):
        self.var_name = name

    def get_variable_value(self):
        return self.var_value

    def set_variable_value(self, value):
        self.var_value = value

    def get_gobal_var_script(self):
        script = self.var_name + " = " + str(self.var_value)
        return script

    def get_local_var_script(self):
        script = "self." + self.var_name + " = " + self.var_value
        return script

    def is_channel(self):
        return True if self.var_type_dic.get(self.var_type) == 3 else False
