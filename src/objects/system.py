from objects.node import Node
from objects.template import Template

"""
    Stores UPPAAL system commands into objects
    1. Converts instance call 
    2. Converts an UPPAAL instance declaration into python script
        - Currently, System class will simply take an entire line
    3. Ignores every comment

    @TODO: Handle parameters

    @AUTHOR: Marco-Backman
"""

class System:
    def __init__(self):
        #instance declaration in full string
        self.instance_declare = [] #key - instance name, value - full script
        self.instances = {}        #key - instance name, value - template
        self.instance_call = []    #will contain the name of the instances

    #If system keyword is raised
    #Rename def name and varaibles - confusing
    #Refactor the functionality this should not contain any script convertation
    def find_templates(self, instace_name : str) -> str:
        try:
            template_name : str = self.instances[instace_name]
            init_function = self.get_init_name(template_name)
            return instace_name + "." + init_function
        except:
            print("Wrong instance name!")

    def get_init_name(self, template : Template) -> str:
        target_node : Node = template.start_state
        script : str = str(target_node.get_name()) + "()"
        return script

    def add_instance_info(self, full_inst : str, instance : str, template : Template):
        print("System added: " + instance + ", " + str(template.name))
        self.instance_declare.append(full_inst)
        self.instances[instance] = template

    def add_call(self, instance_name):
        self.instance_call.append(instance_name)


