import os

"""
    Case 1: One XML file
    Case 2: One XML file with multiple files
    Case 3: No XML with multiple files
    Case 4: No files

    @TODO:

    @AUTHOR: Marco-Backman
"""

default_XML_file_dir = "../data/"
#"upload" path is provided from webserver
download_XML_file_dir = "../../uploads/"
download_predef_file_dir = "../../uploads/"

class FileHandler:

    def __init__(self, xml_file_path, arguments):
        self.xml_file_name = xml_file_path
        self.predef_file_names = []
        self.predef_file_names.extend(arguments)

        #Variables in actual use when returned
        self.xml_relative_path = ""
        self.predef_relative_paths = []

        if(self.check_XML_file() == False):
            raise Exception("XML file not found")

    def locate_file(file_name : str):
        try:
            f = open(file_name, 'r')
            f.close()
        except IOError:
            print("File not found")
            raise Exception

    #Check download first
    def check_XML_file(self):
        #in the download file path
        downloaded_XML_path = download_XML_file_dir + self.xml_file_name
        if os.path.isfile(downloaded_XML_path):
            self.xml_relative_path = downloaded_XML_path
            return True

        #in the data file path
        default_XML_path = default_XML_file_dir + self.xml_file_name
        if os.path.isfile(default_XML_path):
            self.xml_relative_path = default_XML_path
            return True

        #XML File not found - Program termination required
        return False

    #Check if all the files exists
    def check_predef_files(self):
        predef_files = [download_predef_file_dir + f for f in self.predef_file_names];
        self.predef_relative_paths.extend([f for f in predef_files if os.path.isfile(f)]);
        no_files_found = list(set(predef_files) ^ set(self.predef_relative_paths))

        print("existing: %s" % self.predef_relative_paths)
        print("non existing: %s" % no_files_found)

    def get_XML_file(self):
        return self.xml_relative_path

    def get_predef_files(self):
        return self.predef_relative_paths