import re
import xml.etree.ElementTree as ET

from objects.system import System
from objects.global_set import GlobalSet
from objects.template import Template

"""
    Parses XML system tag and info into an object

    Suppose input is given like:
        r1 = Roomba_Test(param1, param2, ...);
        system r1

    Then this will change into:
        r1 = Roomba_Test(param1, param2, ...)
        r1.InitialNodeOfRoomba_Test()

    @TODO: Refactor required - unorganized - inefficient

    @AUTHOR: Marco-Backman
"""

#It can take declared instance, or template name as an instance
class SystemParser:
    def parse_system_instance(line : str, global_sets : GlobalSet):
        elements = line.split("=")
        instance = elements[0].strip()               #instance variable name
        template_str = elements[1].strip()           #instance declaration with params;
        template_str = template_str.replace(")", "") #Roomba_Test(parm1, parm2 ...
        elements = template_str.split("(")
        template_name = elements[0]                  #Only class name
        param_line = elements[1]                     #Parameters
        template : Template = global_sets.get_template_by_name(template_name)
        template.set_instance_name(instance)
        if (template == None): #Error template/init() not found
            print("No template defined")
            return

        sys_obj : System = global_sets.get_system_obj()
        template_list = global_sets.get_templates()
        for temp_template in template_list:
            sys_obj.add_instance_info(line, temp_template.name, temp_template)
        sys_obj.add_instance_info(line, instance, template)
        params = [s.strip() for s in param_line.split(",")]
        sys_obj.add_sys_param(params)

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

    def parse_system(system_content : str, global_sets : GlobalSet):
        new_lines = []
        is_multi_comment = False
        lines = system_content.split("\n")
        for line in lines:
            line = line.strip()
            line, is_multi_comment \
                = SystemParser.remove_comments(line, is_multi_comment)

            if line == "":
                continue

            #system keyword -> Run defined instance
            if "system" in line: # system r1 -> r1.init(params)
                line = line.replace("system", "")
                line = line.replace(";", "")
                line = line.strip()
                sys_obj : System = global_sets.get_system_obj()
                sys_obj.add_call(line) #append - r1

            #Instance declaration
            else:
                line = line.replace(";", "")
                line = line.strip()
                SystemParser.parse_system_instance(line, global_sets)
                new_lines.append(line)
        return new_lines
