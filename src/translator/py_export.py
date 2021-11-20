
class Export:
    def make_file(scripts):  
        with open("./data/output.py","w") as file:
            file.write(scripts)

    def append_to_file(scripts):
        with open("./data/output.py","a") as file:
            file.write(scripts)

    def read_file(fileName):
        with open(fileName, "r") as file:
            return file.read()
