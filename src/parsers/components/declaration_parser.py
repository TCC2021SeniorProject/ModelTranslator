from typing import List
import re

from objects.variable import Variable

"""
    Parses XML declaration tag and info into an object

    @TODO:
    Implement typedef
    Implement const - act as a normal var

    @AUTHOR: Marco-Backman
"""

var_type_dic = {'int'     : 0,
                'bool'    : 1,
                'boolean' : 1,
                'float'   : 2,
                'double'  : 2,
                'channel' : 3,
                'chan'    : 3,
                'array'   : 4,
                'arr'     : 4}

class DeclarationParser:

    def parse_identifier(words : List[str],\
                         var_value : str,\
                         previous_type : str) -> Variable and str:
        if len(words) == 1:
            var_name = words[0].strip()
            var_obj = Variable(previous_type, var_name, var_value)
            return var_obj, previous_type
        elif len(words) == 2:
            var_type = words[0]
            var_name = words[1].strip()
            var_obj = Variable(var_type, var_name, var_value)
            return var_obj, var_type
        elif len(words) == 3:
            var_type = words[0]
            if words[0] == "const":
                var_type = words[1]
                var_name = words[2].strip()
                var_obj = Variable(words[1], var_name , var_value)
                return var_obj, var_type
            elif words[0] == "broadcast":
                var_type = words[1]
                var_name = words[2].strip()
                var_obj = Variable(var_type, var_name , var_value)
                return var_obj, var_type
            elif words[0] == "typedef": #Typedef not implemented
                None, None
            else:
                print("Unsupported type identifier")
                return -1, ""
        else: #Skip error
            return -1, ""

    #Line example: const int k = 2 or const int k
    def parse_attribute(line):
        comma_seperated = re.split(",", line)
        variables : List[Variable] = []
        var_type = ""
        for element in comma_seperated:
            var_value = ""
            element = element.strip()
            words = []
            if "=" in element: #Value assignment exists
                words = element.split("=")
                var_value = (words[len(words) - 1]).strip() #Value
                words = words[:-1] #Truncate right side including '='
                element = ' '.join(words)
                words = element.split()
            else:
                words = element.split()


            var_obj, var_type\
              = DeclarationParser.parse_identifier(words, var_value, var_type)
                        #If variable type is not supportive, skip line
            if (var_type_dic.get(var_type) is None):
                print("Type not supported")
                return -1
            if var_obj == None:
                print("Typedef not supported")
                return -1
            elif var_obj == -1:
                print("Declrartion syntax error on: " + element)
                return -1
            else:
                variables.append(var_obj)
        return variables

    def parse_declaration(declaration_str : str) -> List[Variable]:
        lines = re.split("\n|;", declaration_str)
        lines = [line.strip() for  line in lines]
        total_variales = []
        for line in lines:
            line = line.strip()
            if line == "":      #skip empty
                continue
            elif line[0:2] == "//": #skip comment
                continue
            #Remove constraints
            line = re.sub("\[[^]]*\]", "", line)
            variables = DeclarationParser.parse_attribute(line)
            if variables == -1:
                continue
            for variable in variables:
                total_variales.append(variable)

        return total_variales
