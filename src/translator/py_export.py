from class_gen import Py_class_gen

class Export:
    def make_file(self, scripts):  
        with open("./data/output.py","w") as file:
            file.write(scripts)

    def append_to_file(self, scripts):
        with open("./data/output.py","a") as file:
            file.write(scripts)

    def read_file(self, fileName):
        with open(fileName, "r") as file:
            return file.read()

py_class_gen = Py_class_gen()
export = Export()
export.make_file("\n")
export.append_to_file(py_class_gen.make_default_class_script())
print(export.read_file("./data/output.py"))