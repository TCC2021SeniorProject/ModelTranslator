import sys

from typing import List

from click import argument

from predefine.predef_parser import PredefParser
from objects.global_set import GlobalSet
from translator.py_export import Export
from translator.script_gen import TranslateModel
from predefine.objects.global_obj import PredefGlobalObject
from parsers.XML_parser import generate_model
from file import FileHandler

"""
    XXX Main class
        - Takes UPPAAL model in XML file as an input file
        - Executes parser(translator)
        - Make output in Python scripts
        - Export file to designated path

    @TODO: Consider adding features such as:
                - Get input directory by argument
                - Get output directory by argument

           Add exception handlers to handle any unexpected cases:
                - XML file corruption
                - Cases where transator does not support
                - Invalid input file dir or output file dir

           Resolve coupling problem
                -There are multiple cross importation to be fixed.
                    - Node - Transition, Variable
                    - System - object. modules
                    - GlobalSets - object. modules
                    - Template - Variable

    @AUTHOR: Marco-Backman
    @TARGET USER: UPPAAL users and developers
"""

def generate_scripts(objects : GlobalSet, predef_objects : List[PredefGlobalObject]):
    #Tranlate into python script - single template
    model_translator = TranslateModel(objects, predef_objects)
    model_translator.make_full_scripts()
    scripts = model_translator.get_full_scripts()
    return scripts

#fist argument - request id
#second argument - XML file name
#Third ~ n argument - predefined codes
def main(arguments):
    #Check empty argument
    if len(arguments) == 0:
        raise Exception("Empty arguments")
    file_name = ""
    predef_files = []
    predef_objects : List[PredefGlobalObject] = []
    request_id = arguments[0]
    print("Requestor id: " + request_id)
    if (len(arguments) == 1):
        print("Running with default XML file")
        handler = FileHandler("all_tran_example.xml", [])
        file_name = handler.get_XML_file()
    elif (len(arguments) == 2):
        print("Only XML file is provided")
        handler = FileHandler(arguments[1], [])
        file_name = handler.get_XML_file()
    elif (len(arguments) >= 3):
        print("Full files are provided")
        handler = FileHandler(arguments[1], arguments[2:])
        file_name = handler.get_XML_file()
        handler.check_predef_files()
        predef_files = handler.get_predef_files()

    #Parse XML file into object models
    objects : GlobalSet = generate_model(file_name)

    #Parse predefined script(python) files into object models
    print(predef_files)
    for file in predef_files:
        if (file == None):
            continue
        predefParser = PredefParser(file)
        predefParser.processFile()
        predef_objects.append(predefParser.get_result_data())

    #Match by name
    #Append to a generated script
    scripts = generate_scripts(objects, predef_objects)


    #Export scripts to file
    Export.make_file(scripts, request_id)

if __name__ == '__main__':
    main(sys.argv[1:])
