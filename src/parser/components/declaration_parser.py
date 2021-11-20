import re
from objects.variable import Variable

"""
    Parses XML declaration tag and info into an object

    @TODO: Refactor - messy

    @AUTHOR: Marco-Backman
"""

class DeclarationParser:
    def parse_declaration(declaration_str : str):
        variables = []
        #Check multiple lines
        lines = re.split("\n|;", declaration_str)
        for index, line in enumerate(lines):
            lines[index] = line.strip()
        for line in lines:               #Need refactor
            line = line.strip()
            #disregard comment lines and empty element
            if line[0:2] == "//":
                continue
            elif line == "":
                continue
            attributes = re.split(",", line)
            var_type = ""
            for attribute in attributes:
                var_value = ""
                attribute = attribute.strip()
                words = []
                if "=" in attribute: #Value assignment exists
                    words = attribute.split("=")
                    #right hand is the value
                    var_value = words[len(words) - 1]
                    var_value = var_value.strip()
                    words = words[:-1]
                    attribute = ' '.join(str(e).strip() for e in words)
                    words = attribute.split(" ")
                else:
                    words = attribute.split(" ")

                if len(words) == 1:
                    var_name = words[0].strip()
                    var_obj = Variable(var_type, var_name, var_value)
                    variables.append(var_obj)
                elif len(words) == 2:
                    var_type = words[0]
                    var_name = words[1].strip()
                    var_obj = Variable(var_type, var_name, var_value)
                    variables.append(var_obj)
                else:
                    raise Exception("Something wrong")
        return variables
