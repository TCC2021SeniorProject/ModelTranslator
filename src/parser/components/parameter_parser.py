import xml.etree.ElementTree as ET

from objects.variable import Variable

"""
    Parses XML node tag and info into an object

    @TODO:

    @AUTHOR: Marco-Backman
"""

class ParamParser:
    def parse_param(line : ET):
        params = [s.strip() for s in line.text.split(',')]
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
