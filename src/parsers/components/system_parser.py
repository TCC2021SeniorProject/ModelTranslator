from objects.system import System
from objects.template import Template
from objects.global_set import GlobalSet
from objects.instance import Instance

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
    #Line conatins a full command of instance declaration
    def parse_instance_declare(line : str, global_sets: GlobalSet):
        #Get instance name
        index = line.index("=")
        instance_name = line[:index].strip()

        #Get class name
        remainder = line[index + 1:].strip()
        index = remainder.index("(")
        template_name = remainder[:index].strip()

        #Get Parameter
        end_index = remainder.index(")")
        parameters = remainder[index + 1: end_index].strip()

        #Get template by class name
        target_template : Template \
            = global_sets.get_template_by_name(template_name)

        #Boundary check
        if (target_template == None):
            print("No template defined for :" + template_name)
            return

        #Update system object with parameters
        sys_obj : System = global_sets.get_system_obj()
        #This may produce a single string or list of string
        #Boundary check is required on system object when adding parameters
        params = [s.strip() for s in parameters.split(",")]

        #Add instance to instance object
        print("Instance decaration added as: " + instance_name + " on " + target_template.get_template_name())
        sys_obj.add_instance(instance_name, target_template, params)

    #Add instance name
    def parse_instance_call(call_name, global_sets: GlobalSet):
        system = global_sets.get_system_obj()
        print("Adding calls as: " + call_name)
        system.add_instance_calls(call_name)
        

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
    def parse_system(system_content : str, global_sets):
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
                        SystemParser.parse_instance_call(call.strip(), global_sets)
                #single instance call
                else:
                    #Returns instance call
                    SystemParser.parse_instance_call(line.strip(), global_sets)

            #Instance declaration
            else:
                line = line.strip()
                SystemParser.parse_instance_declare(line, global_sets)
