import re

from objects.template import Template
from objects.global_set import GlobalSet
from objects.instance import Instance
from objects.system import System

"""
    Parses system tag from XML file and form up into object data.

    There are two methods of system calls.
    System section has only instance declaration with optional parameters,
      and instance call with optional parameters

    #Method 1 - Declare name and call

        Suppose input is given like:
            r1 = Roomba_Test(param1, param2, ...);
            system r1

        Then this will change into:
            r1 = Roomba_Test(param1, param2, ...)
            r1.InitialNodeOfRoomba_Test()

    #Method 2 - Call by template name

        Suppose input is given like:
            system r1

        Then this will change into:
            r1.InitialNodeOfRoomba_Test()


    @TODO:

    @AUTHOR: Marco-Backman
"""

#It can take declared instance, or template name as an instance
class SystemParser:
    def add_instance(instance_name : str,
                     template : Template,
                     params : list[str]) -> Instance:
        #Create instance object
        new_instance = Instance(instance_name)
        new_instance.set_parameter(params)

        #Associate instance to template
        template.add_instance(instance_name, new_instance)
        return new_instance

    #instance declaration
    def parse_instance_declare(line : str, global_sets: GlobalSet):

        regex = r"(\w*)[\s]*=[\s]*(\w*)[\s]*\((.*)\)"
        matched_group = re.match(regex, line)
        if (matched_group == None):
            print("Wrong declaration: ", line)
            return
            
        #Get instance name
        instance_name = matched_group[1]

        #Get class name
        template_name = matched_group[2]

        #Get Parameter
        remainder = matched_group[3]
        
        #Get template by class name
        target_template : Template \
            = global_sets.get_template_by_name(template_name)

        #Boundary check
        if (target_template == None):
            print("No template defined for :" + template_name)
            return

        parameters = remainder.split(",")
        #Add instance to instance object
        new_instance = SystemParser.add_instance(instance_name, target_template, parameters)

        #Add to declaration queue to keep the order
        system_obj : System = global_sets.get_system_obj()
        system_obj.add_instance_declaration(new_instance)

    def remove_comments(line : str, is_multi_comment : bool) -> str:
        line = line.strip()
        if is_multi_comment is True:
            if  "*/" in line:
                index = line.index("*/")
                line = line[index + 2:].strip()
                is_multi_comment = False
            else: #Make parser to skip all comment lines by returning empty string
                return "", is_multi_comment
        elif "//" in line: #comment out from that index
            index = line.index("//")
            line = line[:index].strip()
        elif "/*" in line:
            index = line.index("/*")
            line = line[:index].strip()
            is_multi_comment = True
        return line, is_multi_comment

    #Parse XML system syntax into an object
    def parse_system(system_content : str, global_sets : GlobalSet):
        new_lines = ""
        is_multi_comment = False
        for line in system_content.split("\n"):
            line, is_multi_comment \
                = SystemParser.remove_comments(line, is_multi_comment)
            new_lines += line
        commands = new_lines.split(";")
        for line in commands:
            line = line.strip()
            if line == "":
                continue

            #system keyword -> Calls defined instance or calls class(template)
            elif "system" in line: # system r1 -> r1.init(params)
                line = line.replace("system", "")
                #multiple instances can be called by comma-separation
                if ',' in line:
                    calls = line.split(",")
                    for call in calls:
                        global_sets.system_object.add_instance_calls(call.strip())

                #single instance call
                else:
                    #Returns instance call
                    global_sets.system_object.add_instance_calls(line.strip())

            #Instance declaration
            else:
                line = line.strip()
                SystemParser.parse_instance_declare(line, global_sets)
