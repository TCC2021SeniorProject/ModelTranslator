
"""
    Transition's node links cannot be void
    Transition has one to one pointing behavior.
"""
class Transition():
    def __init__(self):
        from objects.node import Node #Avoid cross importation as possible
        self.name  : str
        self.guard : str
        self.sync  : str
        self.assign: str
        self.transition_from : Node
        self.transition_to : Node
        self.visited = False

    def set_from(self, transition_from):
        self.transition_from = transition_from

    def set_to(self, transition_to):
        self.transition_to = transition_to

    def set_name(self, name : str):
        self.name = name

    def set_guard(self, guard : str):
        self.guard = guard

    def set_sync(self, sync : str):
        self.sync = sync

    def set_assign(self, assign : str):
        self.assign = assign

    def get_name(self):
        return self.name

    def get_guard(self):
        return self.guard

    def get_sync(self):
        return self.sync

    def get_assign(self):
        return self.assign

    def get_from_node(self):
        return self.transition_from

    def get_to_node(self):
        return self.transition_to

    def get_from_id(self):
        return self.transition_from.get_id()

    def get_to_id(self):
        return self.transition_to.get_id()