
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