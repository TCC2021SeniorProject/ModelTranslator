import xml.etree.ElementTree as ET

"""
    Parses XML node tag and info into an object

    @TODO:

    @AUTHOR: Marco-Backman
"""

class ParamParser:
    def parse_param(line : ET):
        #Remove all charaters within the enclosed range - ex) int[0,1] a -> int a
        new_line = ""
        open = False
        for char in line.text:
            if char == '[':
                open = True
            elif char == ']':
                open = False
                continue
            if open == False:
                new_line += char
        params = [s.strip() for s in (new_line.split(','))]
        params_name = []
        for param in params:
            param_name = param.split(' ')
            if len(param_name) > 0:
                param_name[1] = param_name[1].replace("&", "")
                params_name.append(param_name[1])
            else:
                param_name[0] = param_name[0].replace("&", "")
                params_name.append(param_name[0])
        return params_name
