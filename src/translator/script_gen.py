from predefine.objects.global_obj import PredefGlobalObject

from objects.global_set import GlobalSet
from objects.template import Template
from objects.variable import Variable
from objects.instance import Instance
from objects.node import Node

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
    def __init__(self, global_set : GlobalSet, predef_objects : list[PredefGlobalObject]):
        self.stack = []
        self.global_set = global_set
        self.templates : list[Template] = global_set.get_templates()
        self.variables : list[Variable] = global_set.get_global_variables()
        self.predef_objects : list[PredefGlobalObject] = predef_objects

        self.start_node = None

        self.global_var_script = ""
        self.entire_script = "import asyncio\nimport time\n"

    #Holds entire single class scripts - class, init(), def().
    def make_class_script(self, template : Template):
        class_gen = ClassScriptGen(template, self.global_set, self.predef_objects)
        class_gen.make_class_scripts()
        class_scripts = class_gen.get_class_script()
        return class_scripts

    #Call this before get_instance_calls()
    def generate_system_declaration_script(self):
        system_dec_script = ""
        system = self.global_set.get_system_obj()
        #Get system call queue
        call : Instance = system.get_next_instance_declaration()
        while (call is not None):
            target_template = self.global_set.get_template_by_instance_name(call.get_instance_name())
            if (target_template is None):
                print("Error in script_gen.py - generate_system_declaration_script()")
                print("template is Null")
                return
            declared_instances : list[Instance] = target_template.get_instance_list()
            parameter_script = ""
            for instance in declared_instances:
                parameter_list = instance.get_parameters()
                for i, param in enumerate(parameter_list):
                    #If that parameter is the last index.(including size of 1 list)
                    if (i == len(parameter_list) - 1):
                        parameter_script += (param)
                    else:
                        parameter_script += (param + ", ")
                #Defined instance format: [name] = [class name]([parameters, ...])
                system_dec_script += instance.get_instance_name() + " = " +\
                    target_template.get_template_name() + "(" +\
                        parameter_script + ")\n"
            call = system.get_next_instance_declaration()
        return system_dec_script

    #Call this after get_instance_delcaration_scripts()
    def generate_system_call_script(self):
        system_call_script = ""
        system = self.global_set.get_system_obj()
        #Get system call queue
        call : str = system.get_next_instance_call()
        while (call is not None):
            target_template = self.global_set.get_template_by_instance_name(call)
            start_node : Node = target_template.get_start()
            system_call_script += "loop.run_until_complete(" + call +\
                "." + start_node.get_name() + \
                "())\n"
            call = system.get_next_instance_call()
        return system_call_script

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
        self.entire_script += self.generate_system_declaration_script()
        self.entire_script += self.generate_system_call_script()

    def get_full_scripts(self):
        return self.entire_script
