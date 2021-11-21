import xml.etree.ElementTree as ET

from objects.node import Node

"""
    Parses XML node tag and info into an object

    @TODO:

    @AUTHOR: Marco-Backman
"""

class NodeParser:
    def parse_node(line : ET):
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
