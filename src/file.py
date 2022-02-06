import os

from typing import Dict, List

"""
    Case 1: One XML file
    Case 2: One XML file with multiple files
    Case 3: No XML with multiple files
    Case 4: No files

    @TODO:

    @AUTHOR: Marco-Backman
"""

#In the data file
default_file_dir = "../data/"
default_file_dir_root = "./ModelTranslator/data/"
#"upload" path is provided from webserver
#For Uploaded XML Files
download_file_dir = "../../upload/"
download_file_dir_root = "./upload/"


class FileHandler:
    def __init__(self, xml_file_path, arguments):
        self.xml_file_name = xml_file_path
        self.predef_file_names = []
        self.predef_file_names.extend(arguments)

        #Variables in actual use when returned
        self.xml_final_path = ""
        self.predef_relative_paths = []

        if(self.check_XML_file() == False):
            raise Exception("XML file not found")

    #Check download first
    def check_XML_file(self):
        #in the download file path from current working path
        downloaded_XML_path = download_file_dir + self.xml_file_name
        downloaded_XML_path = downloaded_XML_path.replace("\\", "/")
        print("Python - XML path: " + downloaded_XML_path)
        if os.path.isfile(downloaded_XML_path):
            print("\tFile found in download path")
            self.xml_final_path = downloaded_XML_path
            return True

        #in the download file path from root path
        downloaded_XML_root_path = download_file_dir_root + self.xml_file_name
        downloaded_XML_root_path = downloaded_XML_path.replace("\\", "/")
        print("Python - XML path: " + downloaded_XML_root_path)
        if os.path.isfile(downloaded_XML_root_path):
            print("\tFile found in download root path")
            self.xml_final_path = downloaded_XML_root_path
            return True

        #in the data file path from current working path
        default_XML_path = default_file_dir + self.xml_file_name
        default_XML_path = default_XML_path.replace("\\", "/")
        print("Python - XML path: " + default_XML_path)
        if os.path.isfile(default_XML_path):
            print("\tFile found in default path")
            self.xml_final_path = default_XML_path
            return True

        #in the data file path from current working path
        default_XML_root_path = default_file_dir_root + self.xml_file_name
        default_XML_root_path = default_XML_root_path.replace("\\", "/")
        print("Python - XML path: " + default_XML_root_path)
        if os.path.isfile(default_XML_root_path):
            print("\tFile found in default root path")
            self.xml_final_path = default_XML_root_path
            return True
        #XML File not found - Program termination required
        return False

    #Check if all the files exists - Refactor required (Functional duplication)
    #   Potential file importation may occur
    #     when the same file exists on more than two different locations
    def check_predef_files(self):
        default_predef_files = [default_file_dir + f for f in self.predef_file_names];
        self.predef_relative_paths.extend([f for f in default_predef_files if os.path.isfile(f)]);

        default_predef_files = [default_file_dir_root + f for f in self.predef_file_names];
        self.predef_relative_paths.extend([f for f in default_predef_files if os.path.isfile(f)]);

        default_predef_files = [download_file_dir + f for f in self.predef_file_names];
        self.predef_relative_paths.extend([f for f in default_predef_files if os.path.isfile(f)]);

        default_predef_files = [download_file_dir_root + f for f in self.predef_file_names];
        self.predef_relative_paths.extend([f for f in default_predef_files if os.path.isfile(f)]);

        #no_files_found = list(set(default_predef_files) ^ set(self.predef_relative_paths))
        print("Matched predefined file path: %s" % self.predef_relative_paths)

    def get_XML_file(self):
        return self.xml_final_path

    def get_predef_files(self) -> List[str]:
        return self.predef_relative_paths