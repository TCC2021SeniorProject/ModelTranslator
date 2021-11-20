from typing import List, Dict
from objects.system import System
from objects.transition import Transition
from objects.template import Template
from objects.variable import Variable

"""
    Holds all the objects that is require for global field in UPPAAL
    XXX This is not used for local level

    @TODO: Finalize sync functionality

    @AUTHOR: Marco-Backman
"""

class GlobalSet:
    def __init__(self):
        self.templates : List[Template] = []
        self.global_variables : List[Variable] = []
        #key - channel name, value - list of transitions
        self.sync_transitions : Dict[Transition] = {}
        self.system_object : System = System()

    def get_template_by_name(self, name) -> Template:
        for template in self.templates:
            if template.get_template_name() == name:
                return template
        return None

    def get_templates(self) -> List[Template]:
        return self.templates

    def set_templates(self, templates : List[Template]):
        self.templates = templates

    def add_template(self, template : Template):
        self.templates.append(template)

    def get_global_variables(self) -> List[Variable]:
        return self.global_variables

    def set_global_variables(self, global_variables : List[Variable]):
        self.global_variables = global_variables

    def add_global_variable(self, global_variable : Variable):
        self.global_variables.append(global_variable)

    def get_sync_transitions(self) -> Dict[str, List[Transition]]:
        return self.sync_transitions

    def add_channel(self, sync_name : str):
        self.sync_transitions[sync_name] = []

    def set_sync_transitions(self, sync_name : str,
                                   sync_transitions : List[Transition]):
        self.sync_transitions[sync_name] = sync_transitions

    def add_sync_transitions(self, sync_name : str,
                                   sync_transition : Transition):
        self.sync_transitions[sync_name].append(sync_transition)

    def get_system_obj(self) -> System:
        return self.system_object

    def set_system_obj(self, system_object : System):
        self.system_object = system_object

    #Call this before get_instance_calls()
    def get_dec_scripts(self):
        script = ""
        declarations = self.system_object.instance_declare
        for declaration in declarations:
            script += declaration + "\n"
        return script

    #Call this after get_instance_delcaration_scripts()
    def get_instance_calls(self):
        script = ""
        calls = self.system_object.instance_call
        for call in calls:
            script += self.system_object.find_templates(call) + "\n"
        return script