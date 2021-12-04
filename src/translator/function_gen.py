from typing import List

from objects.variable import Variable
from objects.template import Template
from objects.node import Node
from objects.transition import Transition
from objects.global_set import GlobalSet

"""
    Script setting info
        Guard  - Conditionals
        Assign - Add variables
        Sync   - Calls sync transition from other template
                 Must be called before any await execution.

    @TODO: Implement auto indentation.

    @AUTHOR: Marco-Backman
"""

class FunctionScriptGen:
    def __init__(self, template : Template, global_set : GlobalSet):
        self.template : Template = template
        self.global_set : GlobalSet = global_set

    def make_constructor(self, param_list, variable_list):
        script = "\tdef __init__(self, "
        for param in param_list:
            script += param + ", "
        script += "):\n"
        #Noting to initialize
        if len(variable_list) == 0:
            script += "\t\tpass\n"
            return  script + "\n"
        for variable in variable_list:
            variable : Variable
            line = "self." + variable.get_variable_name()
            line += " = " + str(variable.get_variable_value())
            script += "\t\t" + line + "\n"
        return script + "\n"

    def make_sync_transtion_script(self, transition : Transition, depth : int):
        script = ""
        #Sync find - '!'
        if transition.is_sync_caller():
            sync_name = transition.sync.get_name()
            sync_transitions : List[Transition] \
              = self.global_set.get_sync_transitions(sync_name)
            #Find targeted node
            if sync_transitions != None:
                for sync_transition in sync_transitions:
                    for i in range(depth):
                        script += "\t"
                    target_node : Node = sync_transition.get_to_node()
                    sync = sync_transition.get_sync()
                    class_name = sync.get_caller_location()
                    script +=  class_name + "()." + target_node.get_name() + "()\n"
        return script

    def make_tranision_to_script(self, transition : Transition):
        script = ""
        line = ""

        # Conditional call(Guard) with sync (and/or) def call
        target_node = transition.get_to_node()
        if transition.guard != None:
            script += "\t\tif " + transition.guard +":\n"
            script += self.make_sync_transtion_script(transition, 3)
            if (len(line) > 1):
                script += line
            script += "\t\t\tawait self." + target_node.get_name() + "()\n"
        else: #No conditional sync (and/or) def call
            script += self.make_sync_transtion_script(transition, 3)
            if (len(line) > 1):
                script += line
            script += "\t\tawait self." + target_node.get_name() + "()\n"

        # Update(Assign), set variable
        if transition.assign != None:
            for assign in transition.assign:
                line += "\t\t\tself." + assign + "\n"
        return script

    def make_function_script(self, node : Node):
        function_scripts = "\tasync def " + node.get_name() + "(self):\n"
        transition_list = node.get_transitions()
        for transition in transition_list:
            transition : Transition
            function_scripts += self.make_tranision_to_script(transition)
        if self.template.is_end(node):
            function_scripts += "\t\texit()\n"
        return function_scripts
