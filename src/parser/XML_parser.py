import re

import xml.etree.ElementTree as ET
from objects.node import Node
from objects.transition import Transition
from objects.model import Model
from objects.variable import Variable

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


"""
   Parse XML elements into objects for model class
   XML data coverted into node, transition objects
"""
class ParseXML():
    #Multiple models not implemented yet

    type_keyword = {'int' : 0,
                    'bool' : 1,
                    'boolean' : 1,
                    'float' : 2,
                    'double' : 2,
                    'string' : 3,
                    'str' : 3}

    def __init__ (self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()
        self.model = Model()

    def get_model(self):
        return self.model

    #checks global declaration / local declaration
    def identify_declaration_tag(self, line):
        return {
            'declaration' : True
        }.get(line.tag, False)

    def identify_template_tag(self, line):
        return {
            'template' : True
        }.get(line.tag, False)

    def identify_location_tag(self, line):
        return {
            'location' : True
        }.get(line.tag, False)

    def identify_transition_tag(self, line):
        return {
            'transition' : True
        }.get(line.tag, False)

    def identify_init_tag(self, line):
        return {
            'init' : True
        }.get(line.tag, False)

    def identify_name_tag(self, line):
        return {
            'name' : True
        }.get(line.tag, False)

    #Make xml line into node
    def set_node(self, line):
        node : Node = None
        id = line.attrib.get("id")
        for sub_tag in line:
            if sub_tag.tag == 'name':
                text = sub_tag.text
                node = Node(id, text)
            #Handle error on void node
            elif sub_tag.tag == 'committed':
                #Not implemented yet
                node.set_commit("??")
        return node

    """
    Implemented types:
        Boolean    - o
        integer    - o
        double     - o
        clocks     - x
        scalar     - x
        arrays     - x
        structures - x
    """
    def supported_var_type(self, var_type):
        var_type = var_type.lower()
        if var_type in self.type_keyword:
            if self.type_keyword[var_type] == 0:
                return 0
            elif self.type_keyword[var_type] == 1:
                return False
            elif self.type_keyword[var_type] == 2:
                return 0.0
            elif self.type_keyword[var_type] == 3:
                return ""
        else:
            return None

    #Parse variable by regex
    def variable_declaration(self, declaration_str : str):
        #Check multiple lines
        lines = re.split("\n|;", declaration_str)
        #trim extra spaces of the line
        for index, line in enumerate(lines):
            lines[index] = line.strip()
        #Need refactor
        for line in lines:
            line = line.strip()
            #disregard comment lines and empty element
            if line[0:2] == "//":
                continue
            elif line == "":
                continue
            attributes = re.split(",", line)
            var_type = ""
            for attribute in attributes:
                var_name = ""
                var_value = ""
                attribute = attribute.strip()
                words = []
                if "=" in attribute: #Value assignment exists
                    words = attribute.split("=")
                    #right hand is the value
                    var_value = words[len(words) - 1]
                    var_value = var_value.strip()
                    words = words[:-1]
                    attribute = ' '.join(str(e).strip() for e in words)
                    words = attribute.split(" ")
                else:
                    words = attribute.split(" ")

                #There will be only cases like
                #type name
                #name
                if len(words) == 1:
                    var_name = words[0].strip()
                    var_obj = Variable(var_type, var_name, var_value)
                    self.model.set_variable(var_obj)
                elif len(words) == 2:
                    var_type = words[0]
                    var_name = words[1].strip()
                    var_obj = Variable(var_type, var_name, var_value)
                    self.model.set_variable(var_obj)
                else:
                    print("Something wrong")

    def set_transition(self, line):
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
                source = self.model.get_node_by_id(source_text)
            elif (sub_tag.tag == 'target'):
                target_text = sub_tag.attrib.get('ref')
                target = self.model.get_node_by_id(target_text)
            elif (sub_tag.tag == 'label'):
                #Transition name
                if sub_tag.attrib.get('kind') == "select":
                    select = sub_tag.text
                #Conditional statement (with variables)
                elif sub_tag.attrib.get('kind') == "guard":
                    guard = sub_tag.text
                #Variable synchroniztion
                elif sub_tag.attrib.get('kind') == "synchronisation":
                    synchronisation = sub_tag.text
                    #Need to be implemented
                #Changing value of existing variable
                elif sub_tag.attrib.get('kind')  == "assignment":
                    assignment = sub_tag.text
                    #Need to be implemented
        temp_transition.set_from(source)
        temp_transition.set_to(target)
        temp_transition.set_name(select)
        temp_transition.set_guard(guard)
        temp_transition.set_sync(synchronisation)
        temp_transition.set_assign(assignment)
        return source, temp_transition

    def set_start(self, node : Node):
        self.model.set_start(node)

    def set_end(self, node : Node):
        self.model.add_end(node)

    def find_end(self, model : Model):
        end_nodes = []
        nodes = model.get_nodes()
        for node in nodes:
            node : Node
            if node.transition_count() == 0:
                end_nodes.append(node)
        return end_nodes

    #Identifying start and end by name
    def identify_start_end_node(self, node : Node):
        if node.get_name().upper() == self.model.START_STATE_TEXT:
            print(node.get_id() + ": setting start node")
            self.set_start(node)
        elif node.get_name().upper() == self.model.END_STATE_TEXT:
            print(node.get_id() + ": Setting end node")
            self.set_end(node)

    #Crucial function of Parser class(Always start from here)
    def convert_to_object(self):
        for elem in self.root.iter():
            if self.identify_declaration_tag(elem):
                #Global variable
                self.variable_declaration(elem.text)
            #Construct template to classes
            elif self.identify_template_tag(elem):
                for lines in elem.findall(".//*"):
                    for line in lines.iter():
                        #Name the template
                        if self.identify_name_tag(line):
                            self.model.set_model_name(line.text)
                        elif self.identify_location_tag(line):
                            node = self.set_node(line)
                            if node == None:
                                continue
                            self.identify_start_end_node(node)
                            self.model.add_node(node)
                        elif self.identify_transition_tag(line):
                            node, transition = self.set_transition(line)
                            #Source node as a departure transition
                            if not (node == None):
                                node.add_transition(transition)
                        #This will override start node identified by name
                        elif self.identify_init_tag(lines):
                            print("Init tag found")
                            node = self.model.get_node_by_id(line.attrib.get('ref'))
                            self.set_start(node)
                        #Local variables - Not implemented yet
                        elif self.identify_declaration_tag(elem):
                            continue
                #Find end node - no transition going out
                end_nodes = self.find_end(self.model)
                for node in end_nodes:
                    self.set_end(node)


"""
    --------------------End of Parser Class-------------------------
"""

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
    if model.get_end_list():
        print("\tEnd state check pass")
        return True
    else:
        print("\tEnd state check failed")
        return False

#  DFS traverse is used - Flooding traverse
def non_conditional_traverse(node : Node, model : Model):
    #type initialization
    transition : Transition
    transitions : list
    transitions = node.get_transitions()

    #base case
    if node.is_visited():
        return
    else:
        node.set_visited()
        if model.is_end(node) == True:
            print("Validity set")
            model.set_valid_graph()

    for transition in transitions:
        print("\tGoing from " + transition.get_from_id()
         + " to " + transition.get_to_id())
        non_conditional_traverse(transition.get_to_node(), model)
    return

#Check the graph is traversable from the start to the end
def check_graph_validity(model : Model):
    print("Check graph validation")
    non_conditional_traverse(model.get_start(), model)
    model.reset_visit() #Reset visitation
    if (model.is_valid_graph()):
        print("\tGraph validity pass")
        return True
    else:
        print("\tGraph validity unpass")
        return False


def check_model(model):
    error_code = True
    error_code = error_code and check_start_node(model)
    error_code = error_code and check_end_node(model)
    error_code = error_code and check_graph_validity(model)
    if (error_code):
        print("All vailitity passed")
        return True
    else:
        print("Error, no pass")
        return False

"""
Starting function
    Returns True/False of the model validity
"""
def generate_model(file_name):
    parser_class = ParseXML(file_name)
    parser_class.convert_to_object()
    model = parser_class.get_model()
    valid_model = check_model(model)
    if valid_model:
        return model
    else:
        return None
