from typing import List, Dict

from predefine.objects.global_obj import PredefGlobalObject

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
    def __init__(self, global_set : GlobalSet, predef_objects : List[PredefGlobalObject]):
        self.stack = []
        self.global_set = global_set
        self.templates : List[Template] = global_set.templates
        self.variables : List[Variable] = global_set.global_variables
        self.predef_objects : List[PredefGlobalObject] = predef_objects

        self.start_node = None

        self.global_var_script = ""
        self.entire_script = "import asyncio\n"

    #Holds entire single class scripts - class, init(), def().
    def make_class_script(self, template : Template):
        class_gen = ClassScriptGen(template, self.global_set, self.predef_objects)
        class_gen.make_class_scripts()
        class_scripts = class_gen.get_class_script()
        return class_scripts

    def make_full_scripts(self):
        #Append imports from predef files
        for predef_object in self.predef_objects:
           for import_obj in predef_object.get_import_objs():
               self.entire_script += import_obj.get_line() + "\n"
        self.entire_script += "\n"

        global_var_script = ""

        #Append global variables scripts
        for global_var in self.variables:
            global_var: Variable
            global_var_script += global_var.get_gobal_var_script() + "\n"
        self.entire_script += global_var_script + "\n"

        #Append each of class scripts
        for template in self.templates:
            self.entire_script += self.make_class_script(template)

        #Instance declaration and calls
        #Use this on Python version lower than 3.7
        self.entire_script += "loop = asyncio.get_event_loop()\n"
        self.entire_script += self.global_set.get_dec_scripts()
        self.entire_script += self.global_set.get_instance_calls()

    def get_full_scripts(self):
        return self.entire_script
