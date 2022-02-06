
class Export:
    def make_file(scripts):
        try:
            with open("./uploads/output.py","w") as file:
                file.write(scripts)
                print("File exported")
        except:
            try:
               with open("../../uploads/output.py","w") as file:
                    file.write(scripts)
                    print("File exported to uploads")
            except:
               raise Exception("File not found")

    def append_to_file(scripts):
        try:
            with open("./uploads/output.py","a") as file:
                file.write(scripts)
                print("File exported")
        except:
            try:
               with open("../../uploads/output.py","a") as file:
                    file.write(scripts)
                    print("File exported to uploads")
            except:
               raise Exception("File not found")

    def read_file(fileName):
        with open(fileName, "r") as file:
            return file.read()
