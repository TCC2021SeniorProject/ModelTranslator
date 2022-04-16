import re

import xml.etree.ElementTree as ET

"""
    Parses XML node tag and info into an object

    @TODO:

    @AUTHOR: Marco-Backman
"""

class ParamParser:
    def parse_param(line : ET):
        strLine = line.text
        new_string = ""
        constraint_opened = False
        #Remove all charaters within the enclosed range - ex) int[0,1] a -> int a
        for char in strLine:
            if (char  == '[' and constraint_opened == False):
                constraint_opened = True
            elif (char  == ']' and constraint_opened == True):
                constraint_opened = False
            elif (constraint_opened == False):
                new_string += char

        params = new_string.split(",")
        params_name = []

        #Matches only charaters from the end until the space/non-charater occurs
        print(params)
        regex = r"(\w*)\s*$"
        for param in params:
            matches = re.search(regex, param)
            if matches:
                params_name.append(matches.group(1))

        return params_name
