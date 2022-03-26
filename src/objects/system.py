from objects.instance import Instance
from objects.template import Template
from objects.node import Node

"""
    Stores UPPAAL system commands into objects
    1. Converts instance call
    2. Converts an UPPAAL instance declaration into python script

    @TODO:

    @AUTHOR: Marco-Backman
"""

class System:
    def __init__(self):
        #instance is called by instance variable name - "instance_name"
        self.instances : dict[Instance] = {}
        #Calls should have either one of two:
        #   1. Class call by default class name without instance declaration
        #   2. Instance call by declared instacne "name"
        self.instance_calls : list[str] = []

    #Find a default function to start on specified instance(template)
    #Returns function name
    def find_init_function(self, instace_name : str) -> str:
        try:
            instance : Instance = self.instances[instace_name]
            template : Template = instance.template
            start_state : Node = template.get_start()
            return start_state.name
        except:
            print("Instance not found!")
            return ""

    def get_instances(self) -> dict[str, Instance]:
        return self.instances

    def get_instance_by_name(self, instance_name : str) -> Instance:
        if instance_name in self.instances.keys():
            return self.instances[instance_name]
        else:
            return ""

    #Adds system declaration details and its template name with its initial function
    def add_instance(self, instance_name : str, template : Template, params):
        new_instance = Instance(instance_name, template)

        new_instance.set_parameter(params)

        #This has to come first before finding and setting init function
        self.instances[instance_name] = new_instance

        initial_function = self.find_init_function(instance_name)
        new_instance.set_init_function(initial_function)

        

    def print_info(self):
        for key in self.instances:
            print("system declared: " + self.instances[key].get_instance_name())

        for calls in self.instance_calls:
            print("system called: " + calls)

    def get_instance_calls(self) -> list[str]:
        return self.instance_calls

    def add_instance_calls(self, instance_name):
        self.instance_calls.append(instance_name)
