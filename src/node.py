from transition import Transition

class Node():

    '''
        id is a non-duplicable number.
        name is a duplicable text field.
        transition is a list with priority
    '''
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.transition_list = []
        print("\tNode added")
    
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def add_transition(self, from_id, to_id, name):
        transition = Transition()
        transition.set_from(from_id)
        transition.set_to(to_id)
        transition.set_name(name)
        self.transition_list.append(transition)
        print("\tTransition added")

    def add_transition(self, transition):
        self.transition_list.append(transition)
        print("\tTransition added")

    def transition_count(self):
        return len(self.transition_list)

    def isEmpty(self):
        return (len(self.transition_list) == 0)