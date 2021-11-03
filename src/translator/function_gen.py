from objects.variable import Variable
from objects.node import Node
from objects.transition import Transition

class FunctionScriptGen:
    def __init__(self, model):
        self.model = model

    def make_constructor(self, param_list, variable_list):
        script = "\tdef __init__(self, "
        for param in param_list:
            script += param + ", "
        script += "):\n"
        script += "\t\tprint('Running constructor')\n"
        for variable in variable_list:
            variable : Variable
            line = "self." + variable.get_variable_name()
            line += " = " + str(variable.get_variable_value())
            script += "\t\t" + line + "\n"
        return script

    """
    Additional script setting
        Guard  - Conditionals
        Assign - Add variables
        Sync   - Check existing variables
    """
    def make_tranision_to_script(self, transition : Transition):
        script = ""
        #Update(Assign), set variable
        line = ""
        if len(transition.assign) > 1:
            line = "\t\tself." + transition.assign + "\n" 

        #Conditional call(Guard)
        target_node = transition.get_to_node()
        if len(transition.guard) > 1:
            script += "\t\tif " + transition.guard +":\n"
            if (len(line) > 1):
                script += "\t" + line
            script += "\t\t\tawait self." + target_node.get_name() + "()\n"
        
        #Normal function call
        else:
            if (len(line) > 1):
                script += line
            script += "\t\tawait self." + target_node.get_name() + "()\n"
        return script

    def make_function_script(self, node : Node):
        transition_list = node.get_transitions()
        function_scripts = "\tasync def " + node.get_name() + "(self):\n"
        for transition in transition_list:
            transition : Transition
            function_scripts += self.make_tranision_to_script(transition)
        if self.model.is_end(node):
            function_scripts += "\t\texit()"
        
        return function_scripts