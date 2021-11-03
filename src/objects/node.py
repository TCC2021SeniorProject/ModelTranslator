from objects.transition import Transition

"""
    Node consists of following elements

    name          : String value used as function name
    id            : Unique identification name.
    commit        : Linkage pointer to other template(class) 
    transition(s) : One direction node pointer linkage.
"""
class Node():

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.commit : str        #Not implemented yet
        self.is_commit = False
        self.visited = False
        self.parameter_list = [] #Not implemented yet.
        self.transition_list = []
        print(name + "Node created")

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_transitions(self):
        return self.transition_list

    def add_transition(self, transition):
        self.transition_list.append(transition)
        print("Transition added")

    def transition_count(self):
        return len(self.transition_list)

    def is_visited(self):
        return self.visited

    def set_visited(self):
        self.visited = True

    def set_unvisited(self):
        self.visited = False
    
    def get_commit(self):
        return self.commit

    def set_commit(self, commit):
        self.is_commit = True
        self.commit = commit