import sys

from objects.global_set import GlobalSet
from translator.py_export import Export
from translator.script_gen import TranslateModel
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

def generate_scripts(objects : GlobalSet):
    #Tranlate into python script - single template
    model_translator = TranslateModel(objects)
    model_translator.make_full_scripts()
    scripts = model_translator.get_full_scripts()
    return scripts

def main(arguments):
    #Required files - must be in full directory format
    file_name = ""
    predef_files = []

    if (len(arguments) == 0):
        print("Running with default XML file")
        handler = FileHandler("test.xml", [])
        file_name = handler.get_XML_file()
    elif (len(arguments) == 1):
        print("Only XML file is provided")
        handler = FileHandler(arguments[0], [])
        file_name = handler.get_XML_file()

    elif (len(arguments) > 1):
        print("Full files are provided")
        handler = FileHandler(arguments[0], arguments[1:])
        file_name = handler.get_XML_file()
        predef_files = handler.get_predef_files()
    else:
        raise Exception("Invalid arguments")


    #Parse and form into model
    objects : GlobalSet = generate_model(file_name)

    #Generate scripts based on the model
    scripts = generate_scripts(objects)

    #Export scripts to file
    Export.make_file(scripts)

if __name__ == '__main__':
    main(sys.argv[1:])
