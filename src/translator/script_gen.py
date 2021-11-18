
from objects.system import System
from objects.template import Model
from objects.variable import Variable

from translator.class_gen import ClassScriptGen
from translator.global_set import GlobalSet


class TranslateModel:
    def __init__(self, objects : GlobalSet):
        self.stack = []
        self.objects = objects
        self.models = objects.models              #list of Model objects
        self.variables = objects.global_variables #list of Variable objects

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
        #Append global variables scripts
        for global_var in self.variables:
            global_var: Variable
            global_var_script += global_var.get_gobal_var_script() + "\n"
        self.entire_script += global_var_script + "\n"
        
        #Append each of class scripts
        for model in self.models:
            self.entire_script += self.make_class_script(model)

        self.entire_script += self.objects.get_dec_scripts() + "\n"
        self.entire_script += self.objects.get_instance_calls() + "\n"

    def get_full_scripts(self):
        return self.entire_script
