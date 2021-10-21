from objects.variable import Variable

class FunctionScriptGen:
    def make_constructor(param_list, variable_list):
        script = "\tdef __init__(self, "
        for param in param_list:
            script += param + ", "
        script += "):\n"
        script += "\t\tprint('Running constructor')\n"
        #make the content - put variable declarations
        for variable in variable_list:
            variable : Variable
            line = "self." + variable.get_variable_name()
            line += "=" + variable.get_variable_value()
            script += "\t\t" + line + "\n"
        return script

