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

    #checks global declaration / local declaration
    def identify_declaration_tag(self, line):
        return {
            'declararion' : True
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

    """
    Accepted types in UPPAAL are:
        Boolean
        integer
        double
        clocks
        scalar
        arrays
        structures
    """
    def supported_var_type(var_type):
        notation = {'int' : 0,
                    'bool' : 1,
                    'double' : 2}

        if notation.has_key(var_type):
            if notation[var_type] == 0:
                return 0
            elif notation[var_type] == 1:
                return False
            elif notation[var_type] == 2:
                return 0.0
        else:
            return None

    """
    #Cases in variable declaration
    # 0. initially start with the assumption
        : int a = 0
        : int b = 10
        : int c
    # 1. variables with assigned initial value
        : int a = 1;
    # 2. variables with no value
    #   : bool a;
    # 3. multiple variables declared separated by ','
        : int a, b, c, d;
        : int a = 1, b = 2, char c = 3;
        : int a=1, b, c, d = 1
    # 4. Will not handle multiple ';' in one line
    # 5. We can throw exception to not to accept unformatted declaration
    """
    def variable_declaration(self, line):
        #trim spaces of the line
        line = line.trim()
        if (line[len(line) - 1] == ';'):
            #Remove ';'
            line = line[0:len(line) - 1]
        #parse - parse by ',' first
        list_of_variables = line.strip(',')

        #parse declaration
        for variable_line in list_of_variables:
            #split line
            elements = variable_line.split(' ')
            #identify supported variable type
            type_definition = self.supported_var_type(elements[0])
            if type_definition == None:
                raise Exception()

            variable = Variable()
            variable_type = elements[0]
            variable_name = elements[1]
            variable_value = type_definition
            elements = variable.strip(' ')
            if (len(elements) > 2):
                if elements[2] == '=':
                    variable_value = elements[3]
                else:
                    print("Wrong type declaration format")
                    raise Exception()
            variable.set_variable_type(variable_type)
            variable.set_variable_name(variable_name)
            variable.set_variable_value(variable_value)
            self.model.set_variable(variable)

    # left fixed to variable name (must be a predefined variable name)
    # middle fixed to notation
    # right fixed to number/data
    # line example: x > 10 / x <= 5.2 / battery == 100
    def parse_guard(self, line):
        #Anything other than these
        notation = {'<' : 0,
                    '>' : 1,
                    '=' : 2,
                    '<=' : 3,
                    '>=' : 4}

        stripped_element = line.strip()

        #format error on given parameter
        if (not (len(stripped_element) == 3)):
            print("Wrong guard parameter given")
            return None

        given_variable = stripped_element[0]
        given_notation = stripped_element[1]
        given_value = stripped_element[2]

        #check if given variable is declared
        variable = self.model.get_variable(given_variable)
        if variable == False:
            return None

        #compare value based on the notation
        if notation.has_key(given_notation):
            print()
            #perform comparison return Ture/False

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
                #Transition name
                if sub_tag.attrib.get('kind') == "select":
                    select = sub_tag.text
                #Conditional statement (with variables)
                elif sub_tag.attrib.get('kind') == "guard":
                    guard = sub_tag.text
                #Variable synchroniztion
                elif sub_tag.attrib.get('kind') == "synchronisation":
                    synchronisation = sub_tag.text
                #Changing value of existing variable
                elif sub_tag.attrib.get('kind')  == "assignment":
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
        for elem in self.root.iter():
            if self.identify_declaration_tag(elem):
                for child in elem.iter():
                    self.variable_declaration(child)
            elif self.identify_template_tag(elem):   
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
def non_conditional_traverse(node : Node, model : Model):
    #type initialization
    transition : Transition
    transitions : list
    transitions = node.get_transitions()

    #base case
    if node.isVisited():
        return
    else:
        node.set_visited()
        if node.get_name().upper() == "END":
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
    if (model.is_valid_graph()):
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
