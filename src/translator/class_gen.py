class Py_class_gen:
    def make_import_script(self):
        str = ""

    def make_default_class_script(self):
        str = ""
        str += "class testClass:\n"
        str += "\t def __init__(self):\n"
        str += "\t\t print('this is a test')\n"
        return str