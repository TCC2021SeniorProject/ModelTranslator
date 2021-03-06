"""
    Transition's node links cannot be void
    Transition has one to one pointing behavior.

    @TODO:
            1. Update more assignment operators
                - 'x:x?y' = ???

    @AUTHOR: Marco-Backman
"""

class Transition():
    def __init__(self):
        #XXX Import at this line to avoid cross importation
        from objects.node import Node
        from objects.sync import Syncronization
        from objects.template import Template
        self.name : str = None
        #stores reformed string
        self.template : Template = None
        self.guard : str  = None
        self.assign : dict[str : str] = {} #key - variable name, value - assignment
        self.transition_from : Node = None
        self.transition_to : Node = None
        self.visited = False
        self.sync : Syncronization = None
        self.sync_caller = False # True: !, False: ?
        self.self_iterating = False

    def get_from_id(self):
        return self.transition_from.get_id()

    def get_from_node(self):
        return self.transition_from

    def set_from(self, transition_from):
        self.transition_from = transition_from

    def get_to_id(self):
        return self.transition_to.get_id()

    def get_to_node(self):
        return self.transition_to

    def set_to(self, transition_to):
        self.transition_to = transition_to

    def get_name(self):
        return self.name

    def set_name(self, name : str):
        self.name = name

    def set_template(self, template):
        self.template = template

    def get_template(self):
        return self.template

    def get_guard(self):
        return self.guard

    def set_guard(self, guard : str):
        self.guard = guard

    def find_variable(self, target_variable) -> bool:
        from parsers.syntax.cpyparser import SyntaxTree
        parse_syntax = SyntaxTree(self.guard)
        parse_syntax.has_variable_name(parse_syntax.root, target_variable)
        if parse_syntax.found:
            return True
        else:
            return False

    def get_sync(self):
        return self.sync

    def set_sync(self, sync_name : str, global_set):
        from objects.sync import Syncronization
        if (sync_name[-1:] == '?'):   # sync: '!'(responder)
            sync_name = sync_name[0:-1]
            self.sync = Syncronization(sync_name)
            self.sync.set_template(self.template)
            self.sync.set_responder(self)
            self.sync_caller = False
            global_set.add_sync_transitions(sync_name, self)
        elif (sync_name[-1:] == '!'): # sync: '?'(caller)
            #This will only be used for name identification
            sync_name = sync_name[0:-1]
            self.sync = Syncronization(sync_name)
            self.sync_caller = True
        else:
            print("Sync syntax error at transition.py, set_sync()")

    def is_sync(self) -> bool:
        if self.sync_caller == True:
            return True
        return False if self.sync == None else True

    def is_sync_caller(self) -> bool:
        if self.sync_caller == True:
            return True
        return False

    def get_assign(self) -> str:
        return self.assign

    #Split with variables and value
    #Assignment can contain multi-line
    def set_assign(self, assign : str):
        assign = assign.replace(":=", "=")
        assign = assign.replace("\t", "")
        assignments = [x.strip() for x in assign.split('\n')]
        for assignment in assignments:
            #Skip any empty line
            if (len(assignment) == 0):
                continue
            assignment_list = assignment.split("=")
            self.assign[assignment_list[0].strip()] = assignment_list[1].strip()

    def set_self_iteration(self):
        self.self_iterating = True

    def is_self_iterating(self):
        return self.self_iterating

    def print_info(self):
        print("\t Transition from: " + self.transition_from.id\
             + " to: " + self.transition_to.id)