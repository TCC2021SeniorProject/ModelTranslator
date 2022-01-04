from objects.template import Template
from objects.node import Node
from objects.transition import Transition
from objects.global_set import GlobalSet

from translator.function_gen import FunctionScriptGen

"""


    @TODO:

    @AUTHOR: Marco-Backman
"""

class ClassScriptGen:
    def __init__(self, template : Template, global_set : GlobalSet):
        self.template = template
        self.class_script = ""
        self.global_set = global_set

    def append_class_def_script(self):
        class_name = self.template.get_template_name()
        self.class_script += "class " + class_name + ":\n"

    #BFS search - store a node to the stack of each visit
    def traverse_template(self):
        queue = []
        stack = []
        queue.append(self.template.get_start())
        while (len(queue) > 0):
            #Remove first and stack up the element
            node : Node = queue[0]
            queue.pop(0)
            node.set_visited()
            stack.append(node)
            #Stack up next nodes by exisiting transitions
            transitions = node.get_transitions()
            for transition in transitions:
                transition : Transition
                to_node = transition.get_to_node()
                if not (to_node.is_visited()):
                    queue.append(to_node)
                    to_node.set_visited()
        return stack

    def append_function_script(self):
        #Make constructor
        parameters = self.template.get_parameters()
        func_script_gen = FunctionScriptGen(self.template, self.global_set)
        script = func_script_gen.make_constructor(parameters)
        self.class_script += script

        #Traverse and stack up the nodes.
        stack = self.traverse_template()
        function_scripts = ""
        while (len(stack) != 0):
            node : Node = stack.pop()
            script = func_script_gen.make_function_script(node)
            function_scripts += script + "\n"
        self.class_script += function_scripts

    #Combines all required scripts
    def make_class_scripts(self):
        self.append_class_def_script()
        self.append_function_script()

    def get_class_script(self):
        return self.class_script
