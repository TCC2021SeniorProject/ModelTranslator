import xml.etree.ElementTree as ET
from node import Node
from transition import Transition
from model import Model

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

#Parse XML elements into objects for model class
class ParseXML():
    #Refactor: vague variable naming
    #XML data coverted into node, transition objects
    data_injected = False #injected into model object
    model = Model()

    def get_model(self):
        return self.model

    #use external parser library
    def parse_XML_into_tree(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    #print all XML attributes - debugging purposes
    def print(self):
        for elem in self.root.iter():
            print(elem.tag)
            print(elem.attrib)

    #refactor required - Violates Function rules #2 (Do one thing) 
    def print_refined_data(self):
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
                        print(id, end = '')
                        print(", ", end = '')
                        print(name_tag.tag , end = '')
                        print(": ", end = '')
                        print(name_tag.text)
                elif (child.tag == 'transition'):
                    source = ""
                    target = ""
                    for transition in child.iter():
                        if (transition.tag == 'transition'):
                            continue
                        elif (transition.tag == 'source'):
                            source = transition.attrib.get('ref')
                        elif (transition.tag == 'target'):
                            target = transition.attrib.get('ref')
                    # data currupted - skip this data
                    if (source == "" or target == ""):
                        continue
                    else:
                        #insert transition to the target node
                        print("from " + source + " to " + target + ", at node:" + id)
    
    #Refactor required - too complicted readability
    def convert_to_object(self):
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
                        # make and add node
                        temp_node = Node(id, name)
                        self.model.add_node(temp_node)
                        #identify start/end state
                        if name.upper() == self.model.START_STATE_TEXT:
                            if self.model.get_start() == None:
                                self.model.set_begin_state(temp_node)
                            else: #Initial and termination state must be only one
                                print("More than one begin state, Skipping")
                        elif name.upper() == self.model.END_STATE_TEXT:
                            if self.model.get_end() == None:
                                self.model.set_end_state(temp_node)
                            else: #Initial and termination state must be only one
                                print("More than one end state, Skipping")

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
                    # data currupted - skip this data
                    if (source == "" or target == ""):
                        continue
                    # connect transition with the given node
                    else:
                        #setup transition object
                        temp_transition = Transition()
                        source_node = self.model.get_node_by_id(source)
                        temp_transition.set_from(source_node)
                        target_node = self.model.get_node_by_id(target)
                        temp_transition.set_to(target_node)
                        #Insert transition to departure node
                        source_node.add_transition(temp_transition)

def check_start_node(model : Model):
    print("Checking start node")
    if (model.get_start()):
        return True
    else:
        return False

def check_end_node(model : Model):
    print("Checking end node")
    if (model.get_end()):
        return True
    else:
        return False

def check_end_state_reachable(model):
    print("Check reachable to the end state")

def check_valid_XML(model):
    print("Check valid XML structure")

def check_loop(model):
    print("Checking infinite loop")
    
def check_transition(model):
    print("Checking transition")

def make_model():
    xml_class = LoadXML()
    parser_class = ParseXML()
    parser_class.parse_XML_into_tree("./data/testCase1.xml")
    parser_class.print_refined_data()
    parser_class.convert_to_object()
    model = parser_class.get_model()
    return model

#If one of the functions returns False error_codes stays False
def check_model(model):
    error_code = True
    error_code = error_code and check_start_node(model)
    error_code = error_code and check_end_node(model)
    #error_code = error_code and check_valid_XML(model)
    #error_code = error_code and check_end_state_reachable(model)
    #error_code = error_code and check_loop(model)
    #error_code = error_code and check_transition(model)

    if (error_code):
        print("Pass")
        return True
    else:
        print("No pass")
        return False

# Traverse the graph without concidering
#  the conditions on each node and transition
#  Since the node has to visit all the nodes,
#  DFS traverse is used
def non_conditional_traverse(node : Node):
    #type initialization
    transition : Transition
    transitions : list
    transitions = node.get_transitions()
    end_state : Node
    for transition in transitions:
        print("Going from " + transition.get_from_id()
         + " to " + transition.get_to_id())
        if node.get_name().upper() == "END":
            end_state = node
        non_conditional_traverse(transition.get_to_node())
    return node


model = make_model()
valid_model = check_model(model)
found_end_state : Node
if (valid_model):
    print("Starting DFS traverse")
    found_end_state = non_conditional_traverse(model.get_start())
else:
    print("Invalid model, terminating")

if (found_end_state):
    print("Connected succussfully")
else:
    print("Did not reach to end state")
