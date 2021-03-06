from re import template
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
            Refactor required.
            - Currently violates one function does one thing.

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

        #Declare global on pre-assigned instances on each template
        templates = self.global_set.get_templates()
        #For current version it appends every template's instances
        for template in templates:
            instances = template.get_instance_list()
            for instance in instances:
                #Assign global instance except itself
                if (template == self.template):
                    continue
                script += "\t\tglobal " + instance.get_instance_name() + "\n"

        #Assign and declare parameters
        for param in params:
            param : str
            line = "self." + str(param)
            line += " = " + str(param)
            script += "\t\t" + line + "\n"
            content_exist = True

        #Declare local variables
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
                task_list = []
                for index, sync_transition in enumerate(sync_transitions):
                    target_node : Node = sync_transition.get_from_node()
                    sync = sync_transition.get_sync()
                    #Check if instance is assigned to local variable
                    class_name : str = sync.get_caller_instance()
                    instances = self.global_set.get_instances_by_template_name(class_name)
                    if (instances is not None):
                        for instance in instances:
                            task_list.append(instance.get_instance_name() + "." + str(target_node.get_name()) + "()")
                    else:
                        task_list.append(class_name + "()." + str(target_node.get_name()) + "()")
                #parallel thread tasks Execution script
                if transition.guard == None:
                    for _ in range(depth - 1): #No guard -> one less indentation
                        script += "\t"
                else:
                    for _ in range(depth):
                        script += "\t"
                script += "await asyncio.gather("
                for task in task_list:
                    script += task +", "
                script += ")\n"

        return script
    '''
        Order of transition function matters!
        1. Thread wait
        2. Sync
        3. Guard
        4. Assignment
        5. Call other transition.
    '''
    #Transition has guard, assignment, sync, empty transition
    def make_tranision_to_script(self,
        transition : Transition,
        delcared_global : dict[str, str]):
        script = ""
        # Conditional call(Guard) with sync (and/or) def call
        target_node = transition.get_to_node()

        #When there is a guard
        if transition.guard != None:

            #Check if guard uses global variable
            for global_variable in self.global_set.global_variables:
                #if there is no global variable being used
                if (transition.find_variable(global_variable.get_variable_name())):
                    global_variable_name = global_variable.get_variable_name()
                    #If this is already declared
                    if global_variable_name not in delcared_global.keys():
                        delcared_global[global_variable_name] = global_variable_name
                        script += "\t\tglobal " + global_variable_name+"\n"
            script += "\t\tif " + str(transition.guard) +":\n"
            
            # Update(Assignment)
            for key in transition.assign:
                isLocal = False
                #If that assignment is part of the local variable, don't append global
                for variable in self.template.variables:
                    if (("self." + variable.get_variable_name()) == key):
                        isLocal = True
                        break
                #Not declared as global
                if key not in delcared_global.keys():
                    #or it is not local
                    if isLocal == False:
                        script += "\t\t\tglobal " + key + "\n"
                #then it is local
                script += "\t\t\t" + key\
                    + " = " + transition.assign[key] + "\n"


            script += "\t\t\tawait asyncio.sleep(0.01)\n"
            script += self.make_sync_transtion_script(transition, 3)
            script += "\t\t\tawait self." + str(target_node.get_name()) + "()\n"

        else: #No gaurd
            for key in transition.assign:
                isLocal = False
                #If that assignment is part of the local variable, don't append global
                for variable in self.template.variables:
                    print("Variable name: ", variable.get_variable_name() , " assginment :" , key)
                    if (("self." + variable.get_variable_name()) == key):
                        print("Trigger")
                        isLocal = True
                        break
                #Not declared as global
                if key not in delcared_global.keys():
                    #or it is not local
                    if isLocal == False:
                        script += "\t\tglobal " + key + "\n"
                script += "\t\t" + key\
                    + " = " + transition.assign[key] + "\n"
            script += "\t\tawait asyncio.sleep(0.01)\n"
            script += self.make_sync_transtion_script(transition, 3)
            script += "\t\tawait self." + str(target_node.get_name()) + "()\n"

        return script

    def make_function_script(self, node : Node):
        #Create function declaration line
        function_scripts = "\tasync def " + str(node.get_name()) + "(self):\n"
        #Eliminates duplicate global variables
        delcared_global : dict[str, str] = {}
        for predef_obj in self.predef_objs:
            predef_function : PredefFunction \
                = predef_obj.get_function_by_name(node.get_name())
            #No match
            if predef_function == None:
                continue
            else:
                function_scripts += str(predef_function.get_partial_content())

        #Append predefined scripts
        transition_list = node.get_transitions()
        for transition in transition_list:
            transition : Transition
            function_scripts += self.make_tranision_to_script(transition, delcared_global)

        if self.template.is_end(node):
            function_scripts += "\t\tpass\n"
        return function_scripts
