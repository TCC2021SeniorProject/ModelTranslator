import parser.XML_parser as Paser
import objects.model as Model

def main():
    model : Model
    #Parse XML to graph
    model = Paser.generate_model("./data/testCase2.xml")
    #Injection? or Run?
    


if __name__ == '__main__':
    main()