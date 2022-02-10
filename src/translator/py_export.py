
class Export:
    def make_file(scripts, XMLFileName : str):
        XMLFileName = XMLFileName.replace(".xml", "")
        print("File name:" + XMLFileName)
        try:
            with open(XMLFileName + "_output.py","w") as file:
                file.write(scripts)
                print("File exported to " + XMLFileName + "_output.py")
        except:
            try:
               with open(XMLFileName + "_output.py","w") as file:
                    file.write(scripts)
                    print("File exported to " + XMLFileName + "_output.py")
            except:
               raise Exception("File not found")

    def append_to_file(scripts, XMLFileName):
        XMLFileName = XMLFileName.replace(".xml", "")
        print("File name:" + XMLFileName)
        try:
            with open(XMLFileName + "_output.py","w") as file:
                file.write(scripts)
                print("File exported to " + XMLFileName + "_output.py","w")
        except:
            try:
               with open(XMLFileName + "_output.py","w") as file:
                    file.write(scripts)
                    print("File exported to " + XMLFileName + "_output.py","w")
            except:
               raise Exception("File not found")

    def read_file(fileName):
        with open(fileName, "r") as file:
            return file.read()
