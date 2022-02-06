from predefine.objects.function_obj import Function
from predefine.objects.import_obj import Function
from predefine.objects.variable_obj import Function

class PredefClass():
    def __init__(self, line):
        self.indented_depth : int = self.count_space(line)
        self.line : str = line.strip()

    def get_indent_depth(self):
        return self.indented_depth

    def get_line(self):
        return self.line

    def get_number_of_tab(self, num_spaces_for_tab):
        remain = self.indented_depth % num_spaces_for_tab
        num_tab = self.indented_depth / num_spaces_for_tab
        if remain != 0:
            raise Exception("Wrong Import Indentation Given")
        return num_tab

