from typing import Dict, List

from objects.system import System
"""
    Holds all the objects that is require for global field in UPPAAL
    XXX This is not used for local level

    @TODO: Add error handler on dictioary access

    @AUTHOR: Marco-Backman
"""

class GlobalSet:
    def __init__(self):
        from objects.template import Template
        from objects.transition import Transition
        from objects.variable import Variable
        self.templates : List[Template] = []
        self.global_variables : List[Variable] = []
        #key - channel name, value - list of Transition
        self.sync_transitions : Dict[List[Transition]] = {}
        self.system_object : System = System()

    def get_template_by_name(self, name):
        for template in self.templates:
            if template.get_template_name() == name:
                return template
        return None

    def get_templates(self):
        return self.templates

    def set_templates(self, templates):
        self.templates = templates

    def add_template(self, template):
        self.templates.append(template)

    def get_global_variables(self):
        return self.global_variables

    def set_global_variables(self, global_variables):
        self.global_variables = global_variables

    def add_global_variable(self, global_variable):
        self.global_variables.append(global_variable)

    def initialize_channel(self, sync):
        sync_name = sync.get_name()
        self.sync_transitions[sync_name] = []

    #Returns list of transitions
    def get_sync_transitions(self, sync_name : str):
        print("Looking for sync name: " + sync_name)
        value = self.sync_transitions[sync_name]
        return value

    #Returns entire dictionary
    def get_sync_dictionary(self):
        return self.sync_transitions

    #Will raise error on wrong name
    def set_sync_transitions(self, sync_name : str,
                                   sync_transitions):
        self.sync_transitions[sync_name] = sync_transitions

    def add_sync_transitions(self, sync_name : str,
                                   sync_transition):
        print("Sync appending to" + str(self.sync_transitions[sync_name]))
        self.sync_transitions[sync_name].append(sync_transition)

    def get_system_obj(self) -> System:
        return self.system_object

    def set_system_obj(self, system_object : System):
        self.system_object = system_object

    def print_tempate_node_transition(self):
        print("----Template node trans info----")
        for template in self.templates:
            template.print_info()

    def print_global_variables(self):
        print("----Global var info----")
        for var in self.get_global_variables():
            print(var.print_info())

    def print_sync_info(self):
        from objects.sync import Syncronization
        from objects.transition import Transition
        print("----Sync info----")
        if len(self.sync_transitions) == 0:
            print("No sync declared\n")
        else:
            for key in self.sync_transitions:
                for transition in self.sync_transitions[key]:
                    transition : Transition
                    sync : Syncronization = transition.get_sync()
                    print("\t sync name: " + sync.get_name())
                    print("\t\t sync location: " + sync.get_caller_location())

    def print_system_info(self):
        print("----System info----")
        if self.system_object == None:
            print("No system declared\n")
        else:
            self.system_object.print_info()
            print()
