from typing import List
from predefine.objects.global_obj import PredefGlobalObject
from predefine.objects.function_obj import PredefFunction
from predefine.objects.import_obj import PredefImport

'''
    Current features:
        1. Only captures functions and imports
        2. Global field executions are ignored
        3. Any other declaration than function and imports are ignored

    @TODO: Refactor required in loops
'''

#Corresponds to a single file
class PredefParser():
    def __init__(self, file):
        self.file = file
        self.global_object : PredefGlobalObject = PredefGlobalObject()

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
        lines = self.readFile()

        skip = False # for multiline comments
        function_object : PredefFunction = None
        def_name = ""
        def_open = False
        def_opening_level = 0
        #Not implemented yet
        class_name = ""
        class_open = False
        class_opening_level = 0

        #Read file line by line
        for i in range (len(lines)):
            #Identify multiple lines
            if skip == True:
                if len(lines > 2):
                    if lines[-3:] == "'''":
                        skip = False
                continue
            line = lines[i]
            #Empty line
            if len(line) == 0:
                continue

            space_num = 0
            #Count indentation
            while(line[space_num] == ' '):
                space_num += 1
            line = line.strip()

            #Global parameters
            index = 0
            temp_line = ""
            #Iteration by single charater
            while index < len(line):
                line.replace("    ", "\t")
                temp_line += line[index]
                
                # def - start capturing until it reaches the same level again
                if temp_line == "def":
                    def_open = True
                    def_name = self.get_name(line[index + 1:].strip())
                    function_object = PredefFunction(line, def_name, space_num)
                    def_opening_level = space_num
                    print("def found: " + def_name)
                    break

                if len(temp_line) > 5:
                    if def_open == True:
                        line.replace("    ", "\t")
                        line = "\t" + line
                        print("Taking lines def content: " + def_name + " : " + line)
                        function_object.append_line(line, space_num)
                    else:
                        print("Not taking lines def content: " + line)
                    break
                # comment
                elif temp_line == '#':
                    break
                # multi-line comment
                elif temp_line == "'''":
                    skip = True
                    break
                #import
                elif temp_line == "from":
                    self.global_object.add_import(PredefImport(line))
                    print("import found")
                    break
                # class
                elif temp_line == "class":
                    class_name = self.get_name(line[index + 1:].strip())
                    print("class found " + class_name)
                    break
                    #get name
                # import
                elif temp_line == "import":
                    self.global_object.add_import(PredefImport(line))
                    print("import found")
                    break
                    #get name
                # global(keyword)
                elif temp_line == "global":
                    print("Global keyword found")
                    break

                line = line.strip()
                if def_open == True and def_opening_level == space_num and len(line) > 2:
                    #Stop captures when opening level and closing level are the same
                    print("Closing def content: " + def_name + " : " + line)
                    #Append function_obj to global_obj
                    self.global_object.add_function(def_name, function_object)
                    def_open = False
                elif def_open == True and (i == len(lines) - 1):
                    line.replace("    ", "\t")
                    line = "\t" + line
                    print("Taking lines def content: " + def_name + " : " + line)
                    function_object.append_line(line, space_num)
                    #Stop captures when opening level and closing level are the same
                    print("Closing def content: " + def_name + " : " + line)
                    #Append function_obj to global_obj
                    self.global_object.add_function(def_name, function_object)
                    def_open = False
                    break
                index += 1
        

    def get_result_data(self) -> PredefGlobalObject:
        return self.global_object