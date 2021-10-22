from objects.variable import Variable

"""
    Transition's node links cannot be void
    Transition has one to one pointing behavior.
"""
class Transition():
    def __init__(self):
        from objects.node import Node #Avoid cross importation as possible
        self.name = None
        self.guard = None    
        self.sync = None
        self.assign = None
        self.transition_from : Node
        self.transition_to : Node
        self.visited = False

    def set_from(self, transition_from):
        self.transition_from = transition_from

    def set_to(self, transition_to):
        self.transition_to = transition_to

    def set_name(self, name : str):
        self.name = name


    def reform_conditional_state(self, guard):
        operator = {
            ">" : 0,
            "<" : 0,
            "==" : 0,
            "=" : 0,
            ">=" : 0,
            "<=" : 0,
        }
        #Left of the operator is variables
        temp_words = guard.split(" ")
        for index, word in enumerate(temp_words):
            if word in operator:
                temp_words[index - 1] = "self." + temp_words[index - 1]
            else:
                continue

        #Reassemble conditional line
        new_line = ""
        for word in temp_words:
            new_line += word + " "
        return new_line

    #Change conditional operators to python-like operators
    def parse_gaurd_operator(self, guard : str):
        guard = guard.replace("||", "or")
        guard = guard.replace("&&", "and")
        return guard

    def parse_assign_operator(self, assign: str):
        assign = assign.replace(":=", "=")
        assign = assign.replace("<=", "=")
        return assign

    def set_guard(self, guard : str):
        guard = self.parse_gaurd_operator(guard)
        self.guard = self.reform_conditional_state(guard)

    def set_sync(self, sync : str):
        self.sync = sync

    def set_assign(self, assign : str):
        assign = self.parse_assign_operator(assign)
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

    """
        Guard  - Conditionals
        Assign - Add variables
        Sync   - Check existing variables
    """
    def make_tranision_to_script(self):
        script = ""
        #Check update(Assign)
        line = ""
        if len(self.assign) > 1:
            line = "\t\tself." + self.assign + "\n" 

        #Check conditional(Guard)
        target_node = self.get_to_node()
        if len(self.guard) > 1:
            script += "\t\tif " + self.guard +":\n"
            if (len(line) > 1):
                script += "\t" + line
            script += "\t\t\tawait self." + target_node.get_name() + "()\n"
        else:
            if (len(line) > 1):
                script += line
            script += "\t\tawait self." + target_node.get_name() + "()"
        return script

    def get_script(self):
        return self.make_tranision_to_script()
        