from objects.model import Model
from objects.model import Variable
from translator.function_gen import FunctionScriptGen

class ClassScriptGen:

    def __init__(self, model : Model):
        self.model = model
        self.class_script = ""
        self.make_class_script()

    def make_class_script(self):
        self.class_script += "class " + self.model.get_model_name() + ":\n"

    def set_class_constructor(self):
        variables = self.model.get_variables()
        script = FunctionScriptGen.make_constructor([], variables)
        self.class_script += script

    def get_class_script(self):
        return self.class_script