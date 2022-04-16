import re

from objects.variable import Variable

"""
    Parses XML declaration tag and info into an object

    @TODO:
    Implement unsupported inline-code features in the future:
        - typedef
        - inline functions with parameters
        - any type of array and clock
        - loops and conditionals
    Current inline-code feature can only perform variable declaration with value assignment

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
    def parse_identifier(words : list[str],\
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
                return -2, ""
            else:
                print("\tUnsupported type identifier")
                return -1, ""
        else: #Skip error
            return -1, ""

    #Line example: const int k = 2 or const int k
    def parse_attribute(line):
        comma_seperated = re.split(",", line)
        variables : list[Variable] = []
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
                print("\tType not supported")
                return -1
            if var_obj == -2:
                print("\tTypedef not supported")
                return -1
            elif var_obj == -1:
                print("\tDeclrartion syntax error on: " + element)
                return -1
            else:
                variables.append(var_obj)
        return variables

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

    def curly_braces(line : str, in_curly_braces : bool):
        pass

    #Begining section of inline code
    def parse_declaration(declaration_str : str) -> list[Variable]:
        lines = re.split("\n|;", declaration_str)
        lines = [line.strip() for  line in lines]
        is_multi_comment = False
        curly_braces = [] #For curly braces identification
        f = [] #For curly braces identification
        total_variales = []
        for line in lines:
            #Comment percolation
            line, is_multi_comment \
                = DeclarationParser.remove_comments(line, is_multi_comment)

            #skip empty line
            if line == "":
                continue
            
            #Skip brackets -> Translator does not interpret function yet.

            #Skip curly brackets -> If whole_command is not empty, means curly braces are not closed yet
            
            #Remove constraints -> Refactor this
            line = re.sub("\[[^]]*\]", "", line) #Remove content surrounded with '[' and ']'
            variables = DeclarationParser.parse_attribute(line)
            if variables == -1:
                continue
            for variable in variables:
                total_variales.append(variable)

        return total_variales
