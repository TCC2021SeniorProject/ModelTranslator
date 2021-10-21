import parser.XML_parser as Paser
from translator.model import TranslateModel

def parse_model(xml_file):
    return Paser.generate_model(xml_file)

def export_to_python_script(model):
    #Tranlate into python script - single template
    model_translator = TranslateModel(model)
    model_translator.append_node_transition_scripts()
    #Export to python file
    model_translator.export_to_file()
    #Read data file
    print(model_translator.read_file())

#Refactor this to take xml_file as argumnent/or prompting input
def main():
    model = parse_model("./data/roomba_test.xml")
    export_to_python_script(model)

if __name__ == '__main__':
    main()