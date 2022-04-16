from objects.instance import Instance

"""
    Stores UPPAAL system commands into objects
    1. Only stores instnace calling sequence in system
    2. All declared instance will be stored in each template with Instance object
    3. This is required to keep the declaration order

    @TODO:

    @AUTHOR: Marco-Backman
"""

class System:
    def __init__(self):
        #Call queues
        self.instance_declare : list[Instance] = []
        self.instance_call : list[str] = []

    def get_next_instance_declaration(self) -> Instance:
        if (len(self.instance_declare) == 0):
            return None
        return self.instance_declare.pop(0)

    def add_instance_declaration(self, instance : Instance):
        self.instance_declare.append(instance)


    def get_next_instance_call(self) -> str:
        if (len(self.instance_call) == 0):
            return None
        return self.instance_call.pop(0)

    def add_instance_calls(self, instance_name):
        self.instance_call.append(instance_name)
