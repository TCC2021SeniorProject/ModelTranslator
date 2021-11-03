
from objects.model import Model
from objects.variable import Variable

from translator.class_gen import ClassScriptGen

class TranslateModel:
    def __init__(self, models, global_variables):
        self.stack = []
        self.models = models              #list of Model()
        self.variables = global_variables #list of Variable()

        self.start_node = None

        self.global_var_script = ""
        self.entire_script = ""
    
    #Holds entire single class scripts - class, init(), def(). 
    def make_class_script(self, model : Model):
        class_gen = ClassScriptGen(model)
        class_gen.make_class_scripts()
        class_scripts = class_gen.get_class_script()
        return class_scripts

    def make_full_scripts(self):
        global_var_script = ""
        class_name = ""
        start_node = ""
        #Append global variables scripts
        for global_var in self.variables:
            global_var: Variable
            global_var_script += global_var.get_gobal_var_script() + "\n"
        self.entire_script += global_var_script
        
        #Append each of class scripts
        for model in self.models:
            self.entire_script += self.make_class_script(model) + "\n"

        #Needs refactor - starting class and node needs to be identified
        #self.entire_script += class_name + "." + start_node.get_name() + "()"

    def get_full_scripts(self):
        return self.entire_script