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
        self.assign : list[str] = None
        self.transition_from : Node = None
        self.transition_to : Node = None
        self.visited = False
        self.sync : Syncronization = None
        self.sync_caller = False # True: !, False: ?

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

    def get_sync(self):
        return self.sync

    def set_sync(self, sync_name : str, global_set):
        from objects.global_set import GlobalSet
        from objects.sync import Syncronization
        if (sync_name[-1:] == '?'):   # sync: '!'(responder)
            sync_name = sync_name[0:-1]
            self.sync = Syncronization(sync_name)
            self.sync.set_template(self.template)
            self.sync.set_responder(self)
            self.sync_caller = False
            global_set : GlobalSet = None
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

    def get_assign(self):
        return self.assign

    def set_assign(self, assign_script : str):
        self.assign = assign_script

    def print_info(self):
        print("\t Transition from: " + self.transition_from.id\
             + " to: " + self.transition_to.id)