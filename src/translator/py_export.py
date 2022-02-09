
class Export:
    def make_file(scripts, XMLFileName):
        XMLFileName = XMLFileName.replace(".xml", "")
        print("File name:" + XMLFileName)
        try:
            with open(XMLFileName + "_output.py","w") as file:
                file.write(scripts)
                print("File exported")
        except:
            try:
               with open(XMLFileName + "_output.py","w") as file:
                    file.write(scripts)
                    print("File exported to uploads")
            except:
               raise Exception("File not found")

    def append_to_file(scripts, XMLFileName):
        XMLFileName = XMLFileName.replace(".xml", "")
        try:
            with open(XMLFileName + "_output.py","w") as file:
                file.write(scripts)
                print("File exported")
        except:
            try:
               with open(XMLFileName + "_output.py","w") as file:
                    file.write(scripts)
                    print("File exported to uploads")
            except:
               raise Exception("File not found")

    def read_file(fileName):
        with open(fileName, "r") as file:
            return file.read()
