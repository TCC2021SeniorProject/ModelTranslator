from translator.function_gen import FunctionScriptGen

# This class is called once for an entire model.
class ClassScriptGen:
    def __init__(self):
        self.class_script = ""

    def make_class_script(self, class_name):
        self.class_script += "class " + class_name + ":\n"
        return self.class_script