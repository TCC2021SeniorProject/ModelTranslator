import xml.etree.ElementTree as ET
from parser.tag_set import TagSet

from objects.global_set import GlobalSet
from objects.node import Node
from objects.template import Template

from parser.components.declaration_parser import DeclarationParser
from parser.components.system_parser import SystemParser
from parser.components.transition_parser import TransitionParser
from parser.components.node_parser import NodeParser

"""
    Parse XML elements into objects for template as a class
    XML data coverted into node, transition objects

    @TODO:
        1. Parse sync
        2. Parse variable constraints
        3. Parse channel and array

    @AUTHOR: Marco-Backman
"""

class ParseXML():
    def __init__ (self, fileName : str):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()
        self.global_sets : GlobalSet = GlobalSet()

    def set_start(self, node : Node, template : Template):
        id = str(node.get_id())
        name = str(node.get_name())
        print("Setting start at :" + id + ", " + name)
        template.set_start(node)

    def set_end(self, node : Node, template : Template):
        id = str(node.get_id())
        name = str(node.get_name())
        print("Setting end at :" + id + ", " + name)
        template.add_end(node)

    def find_end(self, template : Template):
        end_nodes = []
        nodes = template.get_nodes()
        for node in nodes:
            node : Node
            if node.transition_count() == 0:
                print("End node found: ")
                end_nodes.append(node)
        return end_nodes

    """
        XXX Crucial function of Parser class
    """
    def convert_to_object(self):
        #Global declaration
        for elem in self.root.findall("declaration"):
            DeclarationParser.parse_declaration(elem.text)

        for template_xml in self.root.findall("template"):
            template = Template()
            temp_name_set = False
            for line in template_xml.iter():
                node : Node = None
                if TagSet.identify_template_tag(line):
                    continue
                #This assumes every first name tag indicates a class name
                elif TagSet.identify_name_tag(line) and not temp_name_set:
                    print("Class name: " + line.text)
                    template.set_template_name(line.text)
                    temp_name_set = True
                elif TagSet.identify_location_tag(line):
                    node = NodeParser.parse_node(line)
                    if node == None:
                        raise Exception("Node is null")
                    template.add_node(node)
                elif TagSet.identify_transition_tag(line):
                    node, transition = TransitionParser.parse_transition(line, template)
                    if node != None:
                        node.add_transition(transition)
                elif TagSet.identify_init_tag(line):
                    print("Init tag found")
                    #Init may have no name
                    id = line.attrib.get('ref')
                    node = template.get_node_by_id(id)
                    self.set_start(node, template)
                #Local declaration
                elif TagSet.identify_declaration_tag(line):
                    template.set_variables = DeclarationParser.parse_declaration(elem.text)
            #Find end node - no out-going transition
            end_nodes = self.find_end(template)
            
            for node in end_nodes:
                self.set_end(node, template)
            self.global_sets.add_template(template)

        for system in self.root.findall("system"):
            for line in system.iter():
                if TagSet.identify_system_tag(line):
                    self.system_script = SystemParser.parse_system(line, self.global_sets)

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
    XXX Root function of this class
        - This will be called first
        - Returns True/False of the translation success
"""
def generate_model(file_name : str) -> GlobalSet:
    parser_class = ParseXML(file_name)
    parser_class.convert_to_object()
    return parser_class.global_sets
