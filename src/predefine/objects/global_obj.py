from typing import Dict, List

from predefine.objects.function_obj import PredefFunction
from predefine.objects.import_obj import PredefImport
from predefine.objects.variable_obj import PredefVariable

class PredefGlobalObject():
    def __init__(self):
        #Global should always have 0 indentation level
        self.indented_depth : int = 0
        #imports not in the class
        self.global_import : List[PredefImport] = []
        #functions not in the class
        self.global_function : Dict[PredefFunction, str] = {}
        #variables not in the class - need to implement
        self.global_variable : List[PredefVariable] = []

    def get_indent_depth(self):
        return self.indented_depth

    def import_exist(self, target_import : PredefImport):
        return self.search(self.global_import, target_import)

    def add_import(self, target_import : PredefImport):
        self.global_import.append(target_import)

    def get_import_objs(self) -> List[PredefImport]:
        return self.global_import

    def add_function(self, name, target_function : PredefFunction):
        self.global_function[name] = target_function

    def get_function_by_name(self, name) -> PredefFunction:
        if name in self.global_function:
            return self.global_function[name]
        else:
            return None