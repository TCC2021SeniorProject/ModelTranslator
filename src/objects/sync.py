from typing import List

from objects.template import Template
from objects.transition import Transition

"""
    Object for UPPAAL "Sync" keyword
    Contains following infomation:
        -Where the sync is being called
        -Where the sync is pointing to(list of transitions)
        -The name of the sync

    @TODO:

    @AUTHOR: Marco-Backman
"""

class Syncronization():
    def __init__(self, name : str):
        self.instance_name : str = ""
        self.caller_location : Template = None
        self.caller : Transition = None    #!
        self.responder : Transition = None #?
        self.name : str = name

    def get_instance_name(self):
        return self.instance_name

    #Why need this?
    def get_caller_instance(self):
        return self.caller_location.get_template_name()

    def get_caller_location(self):
        return self.caller_location.get_template_name()

    def set_template(self, template: Template):
        self.caller_location : Template = template

    def get_responder(self):
        return self.responder

    def set_responder(self, responder : Transition):
        self.responder = responder

    def get_name(self) -> str:
        return self.name

    def match_caller(self, name: str) -> bool:
        return True if self.caller.name == name else False
