class Instance:
    def __init__ (self, instance_name : str):
        self.instance_name : str = instance_name
        self.parameters : list[str] = []
    
    def get_instance_name(self):
        return self.instance_name

    def get_parameters(self):
        return self.parameters

    def set_parameter(self, parameters : list[str]):
        if isinstance(parameters, list):
            self.parameters = parameters
        else:
            self.parameters.append(parameters)