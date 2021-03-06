import xml.etree.ElementTree as ET

from parsers.components.declaration_parser import DeclarationParser
from parsers.components.node_parser import NodeParser
from parsers.components.system_parser import SystemParser
from parsers.components.transition_parser import TransitionParser
from parsers.components.parameter_parser import ParamParser
from parsers.tag_set import TagSet

from objects.global_set import GlobalSet
from objects.node import Node
from objects.template import Template
from objects.variable import Variable

"""
    Parse XML elements into objects for template as a class
    XML data coverted into node, transition objects

    @TODO:
        1. Parse variable constraints
        2. Parse array
        3. Parse query

    @AUTHOR: Marco-Backman
"""

class ParseXML:
    #Importation required at this field to avoid hidden
    from objects.node import Node
    def __init__ (self, fileName : str):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()
        self.global_set : GlobalSet = GlobalSet()

    def set_start(self, node : Node, template : Template):
        template.set_start(node)

    def set_end(self, node : Node, template : Template):
        template.add_end(node)

    def find_end(self, template : Template) -> list[Node]:
        end_nodes = []
        nodes = template.get_nodes()
        for node in nodes:
            if node.transition_count() == 0:
                print("End node found: ")
                end_nodes.append(node)
        return end_nodes

    #Find sync in global variables and store into sync objects
    def initialize_syncs(self):
        glob_variable_list : list[Variable] \
             = self.global_set.get_global_variables()
        for variable in glob_variable_list:
            if variable.is_channel():
                sync_inst = variable.get_sync_instance()
                self.global_set.initialize_channel(sync_inst)

    def test_print(self):
        self.global_set.print_tempate_node_transition()
        print()
        self.global_set.print_global_variables()
        print()
        self.global_set.print_sync_info()
        print()
        self.global_set.print_system_info()
        print()

    """
        XXX Crucial function of Parser class
    """
    def convert_to_object(self) -> None:
        for elem in self.root.findall("declaration"):
            glob_variable_list = DeclarationParser.parse_declaration(elem.text)
            self.global_set.set_global_variables(glob_variable_list)

        #Find channel
        self.initialize_syncs()

        for template_xml in self.root.findall("template"):
            template = Template()
            temp_name_set = False
            for line in template_xml.iter():
                node : Node = None
                if TagSet.identify_template_tag(line):
                    continue
                #Ordering of tag identification matters
                elif TagSet.identify_name_tag(line) and not temp_name_set:
                    template.set_template_name(line.text)
                    temp_name_set = True

                elif TagSet.identify_location_tag(line):
                    node = NodeParser.parse_node(line)
                    if node == None:
                        raise Exception("Node is null")
                    template.add_node(node)

                elif TagSet.identify_parameter_tag(line):
                    params = ParamParser.parse_param(line)
                    template.add_parameters(params)

                elif TagSet.identify_init_tag(line):
                    #Init may have no name
                    id = line.attrib.get('ref')
                    node = template.get_node_by_id(id)
                    self.set_start(node, template)

                elif TagSet.identify_transition_tag(line):
                    node, transition \
                      = TransitionParser.parse_transition(line, template, self.global_set)
                    if node != None:
                        node.add_transition(transition)
                        template.add_transitions(transition)

                #Local declaration
                elif TagSet.identify_declaration_tag(line):
                    variables = DeclarationParser.parse_declaration(line.text)
                    template.set_variables(variables)

            #Find end node - no out-going transition
            end_nodes = self.find_end(template)
            for node in end_nodes:
                self.set_end(node, template)
            self.global_set.add_template(template)

        #Parse system tag (Only one unique tag)
        system = self.root.find("system")
        self.system_script \
            = SystemParser.parse_system(system.text, self.global_set)
"""
    XXX Root function of this class
        - This will be called first
        - Returns True/False of the translation success
"""
def generate_model(file_name : str) -> GlobalSet:
    parser_class = ParseXML(file_name)
    parser_class.convert_to_object()

    parser_class.test_print()
    return parser_class.global_set
