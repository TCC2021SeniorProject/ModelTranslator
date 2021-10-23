class Variable:
    var_type_dic = {'int' : 0,
                'bool' : 1,
                'boolean' : 1,
                'float' : 2,
                'double' : 2,
                'string' : 3,
                'str' : 3}

    def __init__(self, var_type, var_name, var_value):
        self.var_type = var_type
        self.var_name = var_name
        self.var_value = var_value
        if var_value == "":
            self.set_defualt_value(var_type)
        else:
            self.var_value = var_value

    def set_defualt_value(self, var_type):
        var_type = var_type.lower()
        var_type_index = Variable.var_type_dic.get(var_type, None)
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

    def set_variable_type(self, type):
        self.var_type = type

    def set_variable_name(self, name):
        self.var_name = name

    def set_variable_value(self, value):
        self.var_value = value

    def get_variable_type(self):
        return self.var_type

    def get_variable_name(self):
        return self.var_name

    def get_variable_value(self):
        return self.var_value
