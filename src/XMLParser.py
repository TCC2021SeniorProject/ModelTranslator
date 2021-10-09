import requests
import xml.etree.ElementTree as ET

class LoadXML():

    def __init__(self):
        self.content = ""

    def readFile(self, fileName):
        self.path = fileName
        self.xml_file = open(fileName, "r")
        self.content = self.xml_file.read()
        self.xml_file.close()

    def getContent(self):
        return self.content

class ParseXML():
    def parse_XML_into_tree(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    def print(self):
        trigger = False
        for elem in self.root.iter():
            #make this into hash table
            if (elem.tag == "tempate"):
                trigger = True
            if (trigger):
                print(elem.tag)
                print(elem.attrib)

    def get_template(self):
        
            


class CheckValidXML():
    def check_valid_XML():
        print("Check valid XML structure")

    def check_start_node():
        print("Checking Starting node")

    def check_end_node():
        print("Checking termination node")

    def check_loop():
        print("Checking infinite loop")
    
    def check_transition():
        print("Checking transition")


def main():
    xml_class = LoadXML()
    parser_class = ParseXML()
    #xml_class.readFile("./data/testCase1.xml")
    #print(xml_class.getContent())
    parser_class.parse_XML_into_tree("./data/testCase1.xml")
    parser_class.print()

main()