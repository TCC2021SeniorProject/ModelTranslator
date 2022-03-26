from objects.variable import Variable
from objects.template import Template
from objects.node import Node
from objects.transition import Transition
from objects.global_set import GlobalSet

from predefine.objects.global_obj import PredefGlobalObject
from predefine.objects.function_obj import PredefFunction

"""
    Script setting info
        Guard  - Conditionals
        Assign - Add variables
        Sync   - Calls sync transition from other template
                 Must be called before any await execution.

    @TODO: Implement auto indentation.
            Implement predef class append

    @AUTHOR: Marco-Backman
"""

class FunctionScriptGen:
    def __init__(self, template : Template, global_set : GlobalSet, predef_objs : list[PredefGlobalObject]):
        self.template : Template = template
        self.global_set : GlobalSet = global_set
        self.predef_objs : list[PredefGlobalObject] = predef_objs

    def make_constructor(self, params : list[str]):
        content_exist = False
        script = "\tdef __init__(self, "
        for param in params:
            script += str(param) + ", "
        script += "):\n"
        #Noting to initialize
        for param in params:
            param : str
            line = "self." + str(param)
            line += " = " + str(param)
            script += "\t\t" + line + "\n"
            content_exist = True

        for variable in self.template.get_variables():
            variable : Variable
            line = "self." + str(variable.get_variable_name())
            line += " = " + str(variable.get_variable_value())
            script += "\t\t" + line + "\n"
            content_exist = True

        if content_exist == False:
            script += "\t\tpass\n"
            return  script + "\n"

        return script + "\n"

    def make_sync_transtion_script(self, transition : Transition, depth : int):
        script = ""
        #Sync found - '!'
        if transition.is_sync_caller():
            sync_name = transition.sync.get_name()
            sync_transitions : list[Transition] \
              = self.global_set.get_sync_transitions(sync_name)
            #Find targeted node
            if sync_transitions != None:
                for sync_transition in sync_transitions:
                    for i in range(depth):
                        script += "\t"
                    target_node : Node = sync_transition.get_to_node()
                    sync = sync_transition.get_sync()
                    class_name = sync.get_caller_instance()
                    #sync parameter comes here
                    script +=  str(class_name) + "." + str(target_node.get_name()) + "()\n"
        return script

    def make_tranision_to_script(self, transition : Transition):
        script = ""
        line = ""

        # Conditional call(Guard) with sync (and/or) def call
        target_node = transition.get_to_node()
        if transition.guard != None:
            script += "\t\tif " + str(transition.guard) +":\n"
            script += self.make_sync_transtion_script(transition, 3)
            if (len(line) > 1):
                script += line
            script += "\t\t\tawait self." + str(target_node.get_name()) + "()\n"
        #Assignment exists
        elif transition.assign != None:
            script += "\t\t" + transition.assign +"\n"
            script += self.make_sync_transtion_script(transition, 3)
            if (len(line) > 1):
                script += line
            script += "\t\tawait self." + str(target_node.get_name()) + "()\n"
        else: #No conditional sync (and/or) def call
            script += self.make_sync_transtion_script(transition, 3)
            if (len(line) > 1):
                script += line
            script += "\t\tawait self." + str(target_node.get_name()) + "()\n"

        # Update(Assign), set variable
        if transition.assign != None:
            for assign in transition.assign:
                line += "\t\t\tself." + assign + "\n"
        return script

    def make_function_script(self, node : Node):
        function_scripts = "\tasync def " + str(node.get_name()) + "(self):\n"
        for predef_obj in self.predef_objs:
            print("Getting name from node: " + str(node.get_name()))
            predef_function : PredefFunction \
                = predef_obj.get_function_by_name(node.get_name())
            if predef_function == None:
                print("Name not found from predef: " + str(node.get_name()))
                continue
            else:
                print("Getting name from predef: " + predef_function.name)
            function_scripts += "\n" + str(predef_function.get_partial_content())

        transition_list = node.get_transitions()
        for transition in transition_list:
            transition : Transition
            function_scripts += self.make_tranision_to_script(transition)

        if self.template.is_end(node):
            function_scripts += "\t\texit()\n"
        return function_scripts
