import parser.XML_parser as Paser
import sys

from objects.global_set import GlobalSet
from translator  .py_export import Export
from translator.script_gen import TranslateModel

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

# @TODO Argument should be: 1. execution file 2. input file

# 1. all_tran_example.xml
# 2. fisher.xml
default_input_directory = "./data/all_tran_example.xml"

def identify_system_argument():
    arg_list = sys.argv
    arg_len = len(arg_list)
    if arg_len == 2:
        return arg_list[1]
    elif arg_len > 2:
        raise Exception('Invalid number of arguments are given')
    else:
        print("Using default input file directory: " + default_input_directory)
        return default_input_directory

def locate_file(file_name : str):
    try:
        f = open(file_name, 'r')
        f.close()
    except IOError:
        print("File not found")
        raise

def generate_scripts(objects : GlobalSet):
    #Tranlate into python script - single template
    model_translator = TranslateModel(objects)
    model_translator.make_full_scripts()
    scripts = model_translator.get_full_scripts()
    return scripts

def main():
    #Read XML files
    file_name = ""
    try:
        file_name = identify_system_argument()
        locate_file(file_name)
    except Exception:
        error_type, error_instance, traceback = sys.exc_info()
        error_instance.args = error_instance.args[0]
        raise(error_instance)

    #Parse and form into model
    objects : GlobalSet = Paser.generate_model(file_name)

    #Generate scripts based on the model
    scripts = generate_scripts(objects)

    #Export scripts to file
    Export.make_file(scripts)

if __name__ == '__main__':
    main()
