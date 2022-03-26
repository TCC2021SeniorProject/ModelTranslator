from objects.template import Template

class Instance:
    def __init__ (self, instance_name : str, template : Template):
        self.instance_name : str = instance_name
        self.template : Template = template
        self.parameters : list[str] = []
        self.init_function : str = ""
    
    def get_instance_name(self):
        return self.instance_name

    def get_template(self):
        return self.template

    def get_parameters(self):
        return self.parameters

    def set_parameter(self, parameters : list[str]):
        if isinstance(parameters, list):
            self.parameters = parameters
        else:
            self.parameters.append(parameters)

    def get_init_function(self):
        return self.init_function

    def set_init_function(self, function_name):
        self.init_function = function_name