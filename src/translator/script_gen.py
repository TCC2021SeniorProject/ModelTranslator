from objects.global_set import GlobalSet
from objects.system import System
from objects.template import Template
from objects.variable import Variable

from translator.class_gen import ClassScriptGen

"""
    A root of script generator.
    This will generate outer layer of model to scripts such as:
        1. File importation
        1. Declare global varaibles
        2. Classes

    @TODO: File importation not implemented

    @AUTHOR: Marco-Backman
"""

class TranslateModel:
    def __init__(self, objects : GlobalSet):
        self.stack = []
        self.objects = objects
        self.templates = objects.templates              #list of Template objects
        self.variables = objects.global_variables #list of Variable objects

        self.start_node = None

        self.global_var_script = ""
        self.entire_script = ""
    
    #Holds entire single class scripts - class, init(), def(). 
    def make_class_script(self, template : Template):

        class_gen = ClassScriptGen(template)
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
        for template in self.templates:
            self.entire_script += self.make_class_script(template)

        self.entire_script += self.objects.get_dec_scripts() + "\n"
        self.entire_script += self.objects.get_instance_calls() + "\n"

    def get_full_scripts(self):
        return self.entire_script
