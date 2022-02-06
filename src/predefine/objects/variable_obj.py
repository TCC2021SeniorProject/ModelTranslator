from typing import List

class PredefVariable():
    def __init__(self, name, depth):
        self.name = name
        self.indented_depth : int = depth
        #variable declaration can be more than one line
        self.content : str = ""

    def get_name(self):
        return self.name

    def get_depth(self):
        return self.indented_depth

    #Append whole line including indentation
    def append_line(self, line):
        self.content += "\n" + line

    def get_content(self):
        return self.content
