
class PredefImport():
    def __init__(self, line):
        self.indented_depth : int = self.count_space(line)
        self.line : str = line.strip()

    def count_space(self, line):
        space_num = 0
        if (len(line) == 0):
            return 0
        while(line[space_num] == ' '):
            space_num += 1
        return space_num

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