class Variable:
    """
    Implemented types:
        Boolean    - o
        integer    - o
        double     - o
        clocks     - x
        scalar     - x
        arrays     - x
        structures - x
    """

    var_type_dic = {'int' : 0,
                'bool' : 1,
                'boolean' : 1,
                'float' : 2,
                'double' : 2,
                'string' : 3,
                'str' : 3}

    def __init__(self, var_type, var_name, var_value):
        self.var_type = var_type.lower()
        self.var_name = var_name
        self.var_value = var_value
        var_type_index = Variable.var_type_dic.get(var_type, None)
        if var_value == "":
            self.set_defualt_value(var_type, var_type_index)
        else:
            if var_type_index == 1: #UPPAAL sets boolean value to 0, 1
                if var_value == "0" or var_value == "false":
                    var_value = "False"
                elif var_value == "1" or var_value == "true":
                    var_value = "True"
            self.var_value = var_value

    def set_defualt_value(self, var_type, var_type_index):
        var_type = var_type.lower()
        if var_type_index == 0:
            self.var_value = 0
        elif var_type_index == 1:
            self.var_value = False
        elif var_type_index == 2:
            self.var_value = 0.0
        elif var_type_index == 3:
            self.var_value = ""
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