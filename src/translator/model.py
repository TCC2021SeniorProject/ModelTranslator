from translator.class_gen import ClassScriptGen
from translator.function_gen import FunctionScriptGen
from translator.py_export import Export

from objects.model import Model
from objects.node import Node
from objects.transition import Transition

class TranslateModel:
    def __init__(self, model : Model):
        #Refactor to accept multiple models
        self.model = model
        #Refactor to set model variables to local
        variables = model.get_variables()
        #Refactor to accept class name as template name text
        self.class_name = "TestClass"

        #Refactor this
        self.class_script = "class " + "TestClass" + ":\n"
        self.init_script = FunctionScriptGen.make_constructor([], variables)
        self.def_script = ""
        self.entire_script = ""
        
        #Refactor this to identify start by automation
        self.base_script = self.class_name + "." + model.get_start().get_name() + "()"
        self.stack = []
    
    #BFS search - store a node to the stack of each visit
    def traverse_model(self):
        queue = []
        queue.append(self.model.get_start())
        while (len(queue) > 0):
            #Remove first and stack up the element
            node : Node = queue[0]
            queue.pop(0)
            self.stack.append(node)
            #Stack up next nodes by exisiting transitions
            transitions = node.get_transitions()
            for transition in transitions:
                transition : Transition
                to_node = transition.get_to_node()
                if not (to_node.is_visited()):
                    queue.append(to_node)
                    to_node.set_visited()

    """
        This is used for better readability of the generated code
    """
    def append_node_transition_scripts(self):
        #Traverse and stack up the nodes.
        self.traverse_model()
        #Definitions must be in order.
        while (len(self.stack) != 0):
            node = self.stack.pop()
            node : Node
            #These scripts are constructed at the parsing stages
            node.form_script()
            script = node.get_script()
            if self.model.is_end(node):
                script += "\t\texit()"
            self.append_def_script(script)

    def append_def_script(self, script : str):
        self.def_script += script + "\n\n"

    def assemble_scripts(self):
        self.entire_script += self.class_script + "\n"
        self.entire_script += self.init_script + "\n"
        self.entire_script += self.def_script + "\n"
        self.entire_script += self.base_script + "\n"
    
    def get_entire_scripts(self):
        self.assemble_scripts()
        return self.entire_script

    def export_to_file(self):
        self.export = Export()
        self.export.make_file("")
        self.export.append_to_file(self.get_entire_scripts())

    def read_file(self):
        return self.export.read_file("./data/output.py")