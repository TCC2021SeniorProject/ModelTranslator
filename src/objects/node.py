from objects.transition import Transition

class Node():
    '''
        id:
         - A unique number that can't be duplicated.
        
        name:
         - A duplicable text field.
         - Name has to be function like
            ex1) check_status()
            ex2) get_signal(device_id)
         - It may accpet non-function name, 
            then it must be a built-in function in the translator
    '''
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.commit : str
        self.is_function = False
        self.visited = False
        self.parameter_list = []
        self.transition_list = []
        self.script = "\tasync def " + name + "():\n"
        print("Node added")

    def set_scipt(self, content):
        self.script += content
    
    def get_script(self):
        return self.script

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def isFunction(self):
        return self.is_function

    def add_transition(self, from_id, to_id, name):
        transition = Transition()
        transition.set_from(from_id)
        transition.set_to(to_id)
        transition.set_name(name)
        self.transition_list.append(transition)
        print("Transition added")

    def add_transition(self, transition):
        self.transition_list.append(transition)
        print("Transition added")

    def transition_count(self):
        return len(self.transition_list)

    def isEmpty(self):
        return (len(self.transition_list) == 0)

    def get_transitions(self):
        return self.transition_list

    def set_visited(self):
        self.visited = True

    def set_unvisited(self):
        self.visited = False
    
    def isVisited(self):
        return self.visited

    def set_commit(self, commit):
        self.commit = commit

    def get_commit(self):
        return self.commit

    def form_script(self):
        for transition in self.transition_list:
            transition : Transition
            self.set_scipt(transition.get_script())