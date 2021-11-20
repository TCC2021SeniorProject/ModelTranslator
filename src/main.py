import parser.XML_parser as Paser
import sys

from objects.global_set import GlobalSet
from translator.py_export import Export
from translator.script_gen import TranslateModel

#Argument should be: 1. execution file 2. input file
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

def generate_scripts(objects : GlobalSet):
    #Tranlate into python script - single template
    model_translator = TranslateModel(objects)
    model_translator.make_full_scripts()
    scripts = model_translator.get_full_scripts()
    return scripts

#Refactor this to take xml_file as argumnent/or prompting input
def main():
    #Read XML files
    file_name = ""
    try:
        file_name = identify_system_argument()
    except Exception:
        error_type, error_instance, traceback = sys.exc_info()
        error_instance.args = (error_instance.args[0],)
        raise(error_instance)
    #Parse and form into model
    objects : GlobalSet = Paser.generate_model(file_name)

    #Generate scripts based on the model
    scripts = generate_scripts(objects)

    #Export scripts to file
    Export.make_file(scripts)

#Beginning of the program
if __name__ == '__main__':
    main()
