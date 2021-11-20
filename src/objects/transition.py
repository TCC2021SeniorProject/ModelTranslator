"""
    Transition's node links cannot be void
    Transition has one to one pointing behavior.

    @TODO: make async, guard, assign, sync objects

    @AUTHOR: Marco-Backman
"""

class Transition():
    operator = [">", "<", "==", "=", ">=", "<="]

    def __init__(self):
        #XXX Import at this line to avoid cross importation
        from objects.node import Node
        self.name : str = None
        self.guard : str  = None    
        self.sync : str = None
        self.sync_call = False #True: !, False: ?
        self.assign : str = None
        self.transition_from : Node = None
        self.transition_to : Node = None
        self.visited = False

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

    def reform_conditional_state(self, guard):
        temp_words = guard.split(" ")
        for index, word in enumerate(temp_words):
            if word in self.operator:
                temp_words[index - 1] = "self." + temp_words[index - 1]
            else:
                continue
        #Reassemble conditional line
        new_line = ""
        for word in temp_words:
            new_line += word + " "
        return new_line.strip()

    def get_guard(self):
        return self.guard

    def parse_gaurd_operator(self, guard : str):
        guard = guard.replace("||", "or")
        guard = guard.replace("&&", "and")
        return guard

    def set_guard(self, guard : str):
        guard = self.parse_gaurd_operator(guard)
        self.guard = self.reform_conditional_state(guard)

    def get_sync(self):
        return self.sync

    def set_sync(self, sync : str):
        if (sync[-1:] == '!'):   # sync: '!'(call)
            self.sync_call = True
        elif (sync[-1:] == '?'): # sync: '?'(find)
            self.sync_call = False
        self.sync = sync

    def get_assign(self):
        return self.assign

    def parse_assign_operator(self, assign: str):
        assign = assign.replace(":=", "=")
        assign = assign.replace("<=", "=")
        return assign

    def set_assign(self, assign : str):
        assign = self.parse_assign_operator(assign)
        self.assign = assign
