from calendar import c
import re

from predefine.objects.global_obj import PredefGlobalObject
from predefine.objects.function_obj import PredefFunction
from predefine.objects.import_obj import PredefImport

'''
    Current features:
        1. Only captures functions and imports
        2. Global field executions and Assignments are ignored
        3. Any declaration other than function and imports are ignored

    @TODO:
'''

#Corresponds to a single file
class PredefParser():
    def __init__(self, file):
        self.file = file
        self.predef_global_object : PredefGlobalObject = PredefGlobalObject()

    #Return lines of string
    def readFile (self):
        # Using readlines()
        file_content = open(self.file, 'r')
        return file_content.readlines()

    def parseFile(self, line):
        #count indentation
        if len(line) == 0:
            return

        print(line)

    def get_name(self, line):
        name = ""
        index = 0
        while(index < len(line)):
            if (line[index] == '('):
                break
            name += line[index]
            index += 1
        return name

    #Main function
    def processFile(self):

        #Reuses(overwrites to a new one) on def keyword
        function_object : PredefFunction = None

        def_open = False
        def_indent_count = 0 #For checking def indentation

        #Comments
        multiline_comment_started = False

        #Read file line by line
        lines = self.readFile()
        for line_num, line in enumerate(lines):

            if line_num == len(lines) - 1 and def_open:
                print("End of the line")
                def_open = False

            #Identify comments and ignore them
            if multiline_comment_started == True:
                continue

            if "'''" in line:
                #Multiline comment start
                if multiline_comment_started == True:
                    multiline_comment_started = False
                    index = line.index("'''")
                    line = line[index + 3:].strip() #Takes script after the end of the comment
                #Multiline comment end
                else: 
                    multiline_comment_started = True
                    index = line.index("'''")
                    line = line[:index].strip()

            #Skipline on multiline comments
            elif multiline_comment_started == True:
                continue

            #Remove single line comment
            if "#" in line:
                index = line.index("#")
                line = line[:index].strip()

            #Count indentation (just space or tabs in spaces) - but not tabs
            indent_count = re.findall('^([" "]*)', line)
            indent_count = len(indent_count[0])

            #Skip empty line
            if line.strip() == "":
                continue

            #Remove all trailing and preceding spaces(including indentation)
            line = line.strip()
            
            #store into if def is opend 
            if def_open == True:
                #Check if indentation level is not reduced
                if indent_count < def_indent_count: #end def repeat a same line
                    def_open = False
                else: #Take entire line as instruction of a function 
                    function_object.append_line(line, indent_count)
                    continue


            if (line[0:3] == "def"): #Function declaration
                print("Open def")
                def_open = True
                index = line.index("(")
                def_name = line[3:index].strip() #Only name
                function_object = PredefFunction(line, def_name, line[3:].strip())
                self.predef_global_object.add_function(def_name, function_object)
                def_indent_count = indent_count + 1 # def contents have one more indentation
        
            elif (line[0:4] == "from"): #Import
                self.predef_global_object.add_import(PredefImport(line))

            elif (line[0:6] == "import"): #Import
                self.predef_global_object.add_import(PredefImport(line))

            elif (line[0:5] == "class"): #Class - not implemented
                pass

            elif (line[0:6] == "global"): #Global - not implemented
                pass

    def get_result_data(self) -> PredefGlobalObject:
        return self.predef_global_object