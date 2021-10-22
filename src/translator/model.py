from translator.class_gen import ClassScriptGen
from translator.function_gen import FunctionScriptGen
from translator.py_export import Export

from objects.model import Model
from objects.node import Node
from objects.transition import Transition

class TranslateModel:
    def __init__(self, model : Model):
        self.class_name = "TestClass"
        self.model = model
        py_class_gen = ClassScriptGen()
        self.class_script = py_class_gen.make_class_script(self.class_name)
        variables = model.get_variables()
        self.init_script = FunctionScriptGen.make_constructor([], variables)
        self.def_script = ""
        self.entire_script = ""
        #Refactor this to identify start by automation
        self.base_script = self.class_name + ".Start()"
        self.stack = []
    
    #BFS search - store a node to the stack of each visit
    def traverse_model(self):
        node : Node
        queue = []
        queue.append(self.model.get_start())
        while (len(queue) > 0):
            #Remove first and stack up the element
            node = queue[0]
            queue.pop(0)
            self.stack.append(node)
            #Stack up next nodes by exisiting transitions
            transitions = node.get_transitions()
            for transition in transitions:
                transition : Transition
                to_node = transition.get_to_node()
                if not (to_node.isVisited()):
                    queue.append(to_node)
                    to_node.set_visited()



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
            if (node == self.model.get_end()):
                script += "\t\texit()"
            self.append_def_script(script)

    #Append multiple sets of def scripts
    def append_def_script(self, script : str):
        self.def_script += script + "\n\n"
    
    #Has to be called internally
    def assemble_scripts(self):
        self.entire_script += self.class_script + "\n"
        self.entire_script += self.init_script + "\n"
        self.entire_script += self.def_script + "\n"
        self.entire_script += self.base_script + "\n"

    #This should be called only once
    def get_entire_scripts(self):
        self.assemble_scripts()
        return self.entire_script

    def export_to_file(self):
        self.export = Export()
        self.export.make_file("")
        self.export.append_to_file(self.get_entire_scripts())

    def read_file(self):
        return self.export.read_file("./data/output.py")