import xml.etree.ElementTree as ET

class Parser:

    def __init__(self, filename) -> None:
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()

    def convert_to_object(self):
        index = 0
        for elem in self.root.findall("declaration"):
            print(elem)
        for elem in self.root.iter("template"):
            index += 1
            for child in elem.iter():
                if (elem.tag == "template"):
                    print(elem)
                    continue
                print(str(index) + str(child))


parser = Parser("./data/original_bad.xml")
parser.convert_to_object()