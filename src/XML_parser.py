import xml.etree.ElementTree as ET
from node import Node
from transition import Transition

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
    nodes = []
    transitions = []

    def __init__(self) -> None:
        pass

    def add_transition_by_id(self, id, transition):
        if (len(self.nodes) == 0):
            print("No transition for this node")
            return
        
        for node in self.nodes:
            if (isinstance(node, Node)):
                if (node.get_id() == id):
                    node.add_transition(transition)
                    return
        print("transition not found")
        return

    def parse_XML_into_tree(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    def print(self):
        for elem in self.root.iter():
            print(elem.tag)
            print(elem.attrib)
            
    def print_template(self):
        for elem in self.root.findall('template'):
            for child in elem.findall(".//*"):
                #skip template tag
                if (child.tag == 'template'):
                    continue
                elif (child.tag == 'declaration'):
                    continue
                elif (child.tag == 'location'):
                    for name_tag in child.findall("name"):
                        id = child.attrib.get("id")
                        name = name_tag.text
                        print(id, end = '')
                        print(", ", end = '')
                        print(name_tag.tag , end = '')
                        print(": ", end = '')
                        print(name_tag.text)
                        # add node
                        temp_node = Node(id, name)
                        self.nodes.append(temp_node)
                elif (child.tag == 'transition'):
                    temp_transition = Transition()
                    source = ""
                    target = ""
                    for transition in child.iter():
                        if (transition.tag == 'transition'):
                            continue
                        elif (transition.tag == 'source'):
                            source = transition.attrib.get('ref')
                        elif (transition.tag == 'target'):
                            target = transition.attrib.get('ref')
                    # data curreupted - skip this data
                    if (source == "" or target == ""):
                        continue
                    # connect transition with the given node
                    else:
                        #setup transition object
                        temp_transition = Transition()
                        temp_transition.set_from(source)
                        temp_transition.set_to(target)
                        #insert transition to the target node
                        print("from " + source + " to " + target + ", at node:" + id)
                        self.add_transition_by_id(id, temp_transition)
                        
                        

                        
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
    parser_class.parse_XML_into_tree("./data/testCase1.xml")
    parser_class.print_template()

main()