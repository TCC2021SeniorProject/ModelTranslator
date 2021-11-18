import re
import xml.etree.ElementTree as ET
from parser.tag_set import TagSet

from objects.node import Node
from objects.template import Model
from objects.transition import Transition
from objects.variable import Variable
from translator.global_set import GlobalSet

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
                    'string' : 3,   #Not accepted in UPPAAL - Refactor
                    'str' : 3}      #Not accepted in UPPAAL - Refactor

    def __init__ (self, fileName : str):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()
        self.global_sets : GlobalSet = GlobalSet()

    def parse_node(self, line : ET):
        node : Node = None
        id = line.attrib.get("id")
        for sub_tag in line:
            if sub_tag.tag == 'name':
                text = sub_tag.text
                node = Node(id, text)
            elif sub_tag.tag == 'committed':
                #Not implemented yet
                node.set_commit("??")
        #In case the node is init with no name
        if node == None:
            node = Node(id, "default_init")
        return node

    #Refactor - messy.
    #Parse variable by regex and return variable objects
    def parse_declaration(self, declaration_str : str):
        variables = []
        #Check multiple lines
        lines = re.split("\n|;", declaration_str)
        for index, line in enumerate(lines):
            lines[index] = line.strip()
        for line in lines:               #Need refactor
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

                if len(words) == 1:
                    var_name = words[0].strip()
                    var_obj = Variable(var_type, var_name, var_value)
                    variables.append(var_obj)
                elif len(words) == 2:
                    var_type = words[0]
                    var_name = words[1].strip()
                    var_obj = Variable(var_type, var_name, var_value)
                    variables.append(var_obj)
                else:
                    raise Exception("Something wrong")
        self.global_sets.set_global_variables(variables)

    def parse_transition(self, line : ET, model : Model):
        source : Node = None
        target : Node = None
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
                    #Need to be implemented
                    synchronisation = sub_tag.text
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

    #Refactor required
    def parse_system_instance(self, line : str):
        elements = line.split("=")
        print(elements)
        instance = elements[0].strip()         #r1
        model_str = elements[1].strip()        #Roomba_Test(parm1, parm2 ...);
        model_str = model_str.replace(")", "") #Roomba_Test(parm1, parm2 ...
        elements = model_str.split("(")
        model_name = elements[0]               #Roomba_Test
        param_line = elements[1]               #parm1, parm2 ...
        params = param_line.split(",")

        model = self.global_sets.get_model_by_name(model_name)
        if (model == None): #Error model/init() not found
            print("No model defined")
            return

        sys_obj = self.global_sets.system_object
        sys_obj.add_instance_info(line, instance, model)

    #Refactor required
    """
    r1 = Roomba_Test(param1, param2, ...);
    system r1
    """
    def parse_system(self, et : ET):
        content = et.text
        lines = re.split("\n", content)
        new_lines = []
        for line in lines:
            line = line.strip()
            if line[0:2] == "//":         #Skip comment line
                continue
            elif len(line) < 2:
                continue                  #Skip empty line

            #system keyword -> Run defined instance
            if "system" in line: # system r1 -> r1.init(params)
                line = line.replace("system", "")
                line = line.replace(";", "")
                line = line.strip()
                sys_obj = self.global_sets.system_object
                sys_obj.add_call(line) #append - r1

            else: # r1 = Roomba_Test(param1, param2, ...);
                line = line.replace(";", "")
                line = line.strip()
                self.parse_system_instance(line)
                new_lines.append(line)

        return new_lines

    def set_start(self, node : Node, model : Model):
        id = str(node.get_id())
        name = str(node.get_name())
        print("Setting start at :" + id + ", " + name)
        model.set_start(node)

    def set_end(self, node : Node, model : Model):
        id = str(node.get_id())
        name = str(node.get_name())
        print("Setting end at :" + id + ", " + name)
        model.add_end(node)

    def find_end(self, model : Model):
        end_nodes = []
        nodes = model.get_nodes()
        for node in nodes:
            node : Node
            if node.transition_count() == 0:
                print("End node found: ")
                end_nodes.append(node)
        return end_nodes

    """
        Crucial function of Parser class
    """
    def convert_to_object(self):
        #Global declaration
        for elem in self.root.findall("declaration"):
            self.parse_declaration(elem.text)

        for template in self.root.findall("template"):
            model = Model()
            temp_name_set = False
            for line in template.iter():
                if TagSet.identify_template_tag(line):
                    continue
                #This assumes every first name tag indicates a class name
                elif TagSet.identify_name_tag(line) and not temp_name_set:
                    print("Class name: " + line.text)
                    model.set_model_name(line.text)
                    temp_name_set = True
                elif TagSet.identify_location_tag(line):
                    node = self.parse_node(line)
                    if node == None:
                        raise Exception("Node is null")
                    model.add_node(node)
                elif TagSet.identify_transition_tag(line):
                    node, transition = self.parse_transition(line, model)
                    if not (node == None):
                        node.add_transition(transition)
                elif TagSet.identify_init_tag(line):
                    print("Init tag found")
                    #Init may have no name
                    id = line.attrib.get('ref')
                    node = model.get_node_by_id(id)
                    self.set_start(node, model)
                #Local declaration
                elif TagSet.identify_declaration_tag(line):
                    model.set_variables = self.parse_declaration(elem.text)
            #Find end node - no transition going out
            end_nodes = self.find_end(model)
            
            #Finalize single template
            for node in end_nodes:
                self.set_end(node, model)
            self.global_sets.add_model(model)

        for system in self.root.findall("system"):
            for line in system.iter():
                if TagSet.identify_system_tag(line):
                    #Refactor this to store into object rather than in text
                    self.system_script = self.parse_system(line)

        for queries in self.root.findall("queries"):
            for line in queries.iter():
                #Not implemented
                if TagSet.identify_queries_tag:
                    pass
                #Not implemented
                elif TagSet.identify_query_tag:
                    pass
                #Not implemented
                elif TagSet.identify_formula_tag:
                    pass
                #Not implemented
                elif TagSet.identify_comment_tag:
                    pass
"""
Root function of this class
    - This will be called first
    - Returns True/False of the model validity
"""
def generate_model(file_name : str) -> GlobalSet:
    parser_class = ParseXML(file_name)
    parser_class.convert_to_object()
    return parser_class.global_sets
