from typing import List

from predefine.objects.variable_obj import PredefVariable

'''
    @TODO : indentation need to be aligned to original location
'''

class SingleLine():
    def __init__(self, line, spaces):
        self.line : str = line
        self.spaces : int = spaces

    def get_line_with_indent(self):
        temp_line = ""
        for i in range(int(self.spaces / 4)):
            temp_line += "\t"
        return temp_line + self.line

class PredefFunction():
    #line as trimmed line
    def __init__(self, line, name, depth):
        self.name : str = name
        self.declaration : str = line
        #Not neccesarily needed
        self.variable : List[PredefVariable] = []
        self.content : List[SingleLine] = []
        self.indented_depth : int = depth

    def get_name(self):
        return self.name

    def get_depth(self):
        return self.indented_depth

    #Append whole line including indentation
    def append_line(self, line, spaces):
        self.content.append(SingleLine(line, spaces))

    def get_content(self) -> List[SingleLine]:
        return self.content

    #Returns content without function declaration
    def get_partial_content(self):
        full_script = ""
        for i in range(len(self.content)):
            full_script += self.content[i].get_line_with_indent() + "\n"
        return full_script + "\n"

    #Returns full content with declaration
    def get_full_content(self):
        full_script = self.declaration
        for i in range(len(self.content)):
            full_script += self.content[i].get_line_with_indent() + "\n"
        return full_script + "\n"

    def get_declaration(self):
        return self.declaration