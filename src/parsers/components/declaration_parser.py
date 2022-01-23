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

class DeclarationParser:
    def parse_identifier(words : List[str],\
                         var_value : str,\
                         previous_type : str)\
                         -> Variable and str:
        if len(words) == 1:
            var_obj = Variable(previous_type, words[0].strip(), var_value)
            return var_obj, previous_type
        elif len(words) == 2:
            var_type = words[0]
            var_obj = Variable(var_type, words[1].strip(), var_value)
            return var_obj, var_type
        elif len(words) == 3:
            var_type = words[0]
            if words[0] == "const":
                var_obj = Variable(var_type, words[2].strip(), var_value)
                return var_obj, var_type
            elif words[0] == "typedef":
                None, None
            else:
                print("Unsupported type identifier")
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
            if var_obj == None:
                print("Typedef not supported")
            elif var_obj == -1:
                print("Declrartion syntax error on: " + element)
            else:
                variables.append(var_obj)
        return variables

    def parse_declaration(declaration_str : str) -> List[Variable]:
        lines = re.split("\n|;", declaration_str)
        lines = [line.strip() for  line in lines]
        total_variales = []
        for line in lines:
            line = line.strip()
            if line[0:2] == "//": #skip comment
                continue
            elif line == "":      #skip empty
                continue
            #Remove constraints
            line = re.sub("\[[^]]*\]", "", line)
            print(line)
            variables = DeclarationParser.parse_attribute(line)
            for variable in variables:
                total_variales.append(variable)

        return total_variales
