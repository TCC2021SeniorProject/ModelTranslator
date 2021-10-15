import xml.etree.ElementTree as ET
from objects.node import Node
from objects.transition import Transition
from objects.model import Model

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
    #XML data coverted into node, transition objects
    data_injected = False #injected into model object
    model = Model()

    def get_model(self):
        return self.model

    #use external parser library
    def parse_XML_into_tree(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    def identify_location_tag(self, line):
        return {
            'location' : True
        }.get(line.tag, False)

    def identify_transition_tag(self, line):
        return {
            'transition' : True
        }.get(line.tag, False)

    def set_node(self, line):
        node : Node
        id = line.attrib.get("id")
        for sub_tag in line:
            if sub_tag.tag == 'name':
                text = sub_tag.text
                node = Node(id, text)
            elif sub_tag.tag == 'committed':
                #Update required
                node.set_commit("??")
        return node

    def set_transition(self, line, model : Model):
        #Initial declaration
        source : Node
        target : Node
        select = ""
        guard = ""
        synchronisation = ""
        assignment = ""
        temp_transition = Transition()
        
        for sub_tag in line:
            if (sub_tag.tag == 'source'):
                source_text = sub_tag.attrib.get('ref')
                source = model.get_node_by_id(source_text)
            elif (sub_tag.tag == 'target'):
                target_text = sub_tag.attrib.get('ref')
                target = model.get_node_by_id(target_text)
            elif (sub_tag.tag == 'label'):
                if sub_tag.attrib.get('kind') == "select":
                    select = sub_tag.text
                if sub_tag.attrib.get('guard'):
                    guard = sub_tag.text
                if sub_tag.attrib.get('synchronisation'):
                    synchronisation = sub_tag.text
                if sub_tag.attrib.get('assignment'):
                    assignment = sub_tag.text
        temp_transition.set_from(source)
        temp_transition.set_to(target)
        temp_transition.set_name(select)
        temp_transition.set_guard(guard)
        temp_transition.set_sync(synchronisation)
        temp_transition.set_assign(assignment)
        return source, temp_transition

    def identify_start_end_node(self, node : Node, model : Model):
        if node.get_name().upper() == model.START_STATE_TEXT:
            print(node.get_id() + ": setting start node")
            model.set_start_state(node)
        elif node.get_name().upper() == model.END_STATE_TEXT:
            print(node.get_id() + ": Setting end node")
            model.set_end_state(node)
        return model

    def convert_to_object(self):
        for elem in self.root.findall('template'):
            for child in elem.findall(".//*"):
                for lines in child.iter():
                    #location tag match
                    if self.identify_location_tag(lines):
                        node = self.set_node(lines)
                        if node == None:
                            continue
                        self.model = self.identify_start_end_node(node, self.model)
                        self.model.add_node(node)
                    elif self.identify_transition_tag(lines):
                            node, transition = self.set_transition(lines, self.model)
                            #Source node as a departure transition
                            if not (node == None):
                                node.add_transition(transition)

def check_start_node(model : Model):
    print("Checking start node")
    if (model.get_start()):
        print("\tStart state check pass")
        return True
    else:
        print("\tStart state check failed")
        return False

def check_end_node(model : Model):
    print("Checking end node")
    if (model.get_end()):
        print("\tEnd state check pass")
        return True
    else:
        print("\tEnd state check failed")
        return False

#  DFS traverse is used - Flooding traverse
def non_conditional_traverse(node : Node):
    #type initialization
    transition : Transition
    transitions : list
    transitions = node.get_transitions()
    end_state : Node

    #base case
    if node.isVisited():
        return
    else:
        node.set_visited()

    for transition in transitions:
        print("\tGoing from " + transition.get_from_id()
         + " to " + transition.get_to_id())
        if node.get_name().upper() == "END":
            end_state = node
        non_conditional_traverse(transition.get_to_node())
    return node

#Check the graph is traversable from the start to the end
def check_graph_validity(model):
    print("Check graph validation")
    found_end_state = non_conditional_traverse(model.get_start())
    if (found_end_state):
        print("\tGraph validity pass")
        return True
    else:
        print("\tGraph validity unpass")
        return False

def check_loop(model):
    print("Checking infinite loops")
    
def check_transition(model):
    print("Checking invalid transitions")

#Only passes when everything passes
def check_model(model):
    error_code = True
    error_code = error_code and check_start_node(model)
    error_code = error_code and check_end_node(model)
    error_code = error_code and check_graph_validity(model)
    #error_code = error_code and check_loop(model)
    #error_code = error_code and check_transition(model)

    if (error_code):
        print("All vailitity passed")
        return True
    else:
        print("Error, no pass")
        return False

#Returns True/False of the model validity
def generate_model(file_name):
    parser_class = ParseXML()
    parser_class.parse_XML_into_tree(file_name)
    parser_class.convert_to_object()
    model = parser_class.get_model()
    valid_model = check_model(model)
    return valid_model
