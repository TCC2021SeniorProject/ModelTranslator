import requests
import xml.etree.ElementTree as ET

class LoadXML:
    def readFile(fileName):
        path = fileName


class CheckValidXML:
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
    text_file = open("./data/testCase1.xml", "r")
    data = text_file.read()
    text_file.close()
    print(data)
    #xmlFileLoad = LoadXML.readFile(filename)

main()