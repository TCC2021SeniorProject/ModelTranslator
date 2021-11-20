import xml.etree.ElementTree as ET

from objects.node import Node
from objects.template import Template
from objects.transition import Transition

"""
    Parses XML transition tag and info into an object

    @TODO:

    @AUTHOR: Marco-Backman
"""

class TransitionParser:
    def parse_transition(line : ET, template : Template):
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
                source = template.get_node_by_id(source_text)
            elif (sub_tag.tag == 'target'):
                target_text = sub_tag.attrib.get('ref')
                target = template.get_node_by_id(target_text)
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
                    synchronisation = sub_tag.text.strip()
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
