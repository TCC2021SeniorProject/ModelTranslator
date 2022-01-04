import xml.etree.ElementTree as ET
from parser.syntax.cpyparser import SyntaxTree
from typing import List

from objects.global_set import GlobalSet
from objects.node import Node
from objects.template import Template
from objects.transition import Transition

"""
    Parses XML transition tag and info into an object

    @TODO:

    @AUTHOR: Marco-Backman
"""

class TransitionParser:
    def parse_transition(line : ET,
                         template : Template,
                         global_set : GlobalSet):
        source : Node = None
        target : Node = None
        select : str = ""
        guard : str = None
        synchronization : str = None
        assignment : str = None
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
                    synchronization : str = sub_tag.text.strip()
                #Changing value of existing variable
                elif sub_tag.attrib.get('kind')  == "assignment":
                    assignment = sub_tag.text
                    #Need to be implemented
        temp_transition.set_from(source)
        temp_transition.set_to(target)
        temp_transition.set_name(select)
        temp_transition.set_template(template)
        if guard != None:
            print("From " + guard)
            guard = TransitionParser.reform_conditional_state(guard)
            print("To " + guard)
            temp_transition.set_guard(guard)
        if assignment != None:
            print("From " + assignment)
            assignment = TransitionParser.parse_assign_operator(assignment)
            print("To " + assignment)
            temp_transition.set_assign(assignment)
        if synchronization != None:
            temp_transition.set_sync(synchronization, global_set)
        return source, temp_transition

    def parse_assign_operator(assign_script: str) -> List[str]:
        assign_list = [assign.strip() for assign in assign_script.split(",")]
        assign_list = [TransitionParser.reform_assingment_state(assign) for assign in assign_list]
        assign_script = ""
        for assign in assign_list:
            assign_script += assign
        return assign_script

    def reform_assingment_state(statement : str):
        synt_tree = SyntaxTree(statement)
        statement = synt_tree.get_conditional_script(synt_tree.root, "")
        return statement


    def reform_conditional_state(statement : str):
        synt_tree = SyntaxTree(statement)
        statement = synt_tree.get_conditional_script(synt_tree.root, "")
        return statement
