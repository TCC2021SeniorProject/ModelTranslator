import sys
import parser.XML_parser as Paser

from translator.model import TranslateModel

#Argument should be: 1. execution file 2. input file
default_input_directory = "./data/roomba_test.xml"

def identify_system_argument():
    arg_list = sys.argv
    arg_len = len(arg_list)
    if arg_len == 2:
        return arg_list[1]
    elif arg_len > 2:
        raise Exception('Invalid number of arguments are given')
    else:
        print("Using default input file directory: " + default_input_directory)
        return "./data/roomba_test.xml"

def parse_model(xml_file):
    validation = Paser.generate_model(xml_file)
    if validation == None:
        print("Invalid model given, terminating")
        return -1
    else:
        return Paser.generate_model(xml_file)

def export_to_python_script(model):
    #Tranlate into python script - single template
    model_translator = TranslateModel(model)
    model_translator.append_node_transition_scripts()
    #Export to python file
    model_translator.export_to_file()

#Refactor this to take xml_file as argumnent/or prompting input
def main():
    file_name = ""
    try:
        file_name = identify_system_argument()
    except Exception:
        error_type, error_instance, traceback = sys.exc_info()
        error_instance.args = (error_instance.args[0],)
        raise(error_instance)
    model = parse_model(file_name)

    if model != -1:
        export_to_python_script(model)

#Beginning of the program
if __name__ == '__main__':
    main()