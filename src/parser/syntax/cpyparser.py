"""
    XXX This is a module file that only does one job:
        convert operational syntax to python scrypt
          input:  ++b&&(!a)
          output: b += 1 and not a

    @TODO: Separeate sections for assignment, conditionals, inline-codes

    @AUTHOR: Marco-Backman

    @TARGET USER: Users who requires their single line of C assingment script and
                  conditional statement script to be converted to Python code
"""

#Left - C syntax, Right - Python syntax
conditional_single_operator = { "&" : 1,
                                "|" : 1,
                                ">" : 3,
                                "<" : 3,
                                "=" : 3,
                                ">" : 3,
                                "<" : 3,
                                "!" : 4,
                                ":" : 5,
                                "+" : 5,
                                "-" : 5,
                                "*" : 6,}

conditional_operator = {"&&" : "and",
                        "||" : "or",
                        ">=" : ">=",
                        "<=" : "<=",
                        "==" : "==",
                        ">" : ">",
                        "<" : "<",
                        "!=" : "!=",
                        "=" : "=",
                        "<=" : "=",
                        ":=" : "=",
                        "//=" : "//=",
                        "//=" : "//=",
                        "+=" : "+=",
                        "-=" : "-=",
                        "/=" : "/=",
                        "*=" : "*=",
                        "%=" : "%=",
                        "&=" : "&=",
                        "|=" : "|=",
                        "^=" : "^=",}

expression = {'!' : 'not ',
              '(' : '(',
              '++' : "+= 1",
              '--' : "-= 1"}

class Node:
    #Four directional node
    def __init__(self, value):
        self.parent : Node = None
        self.left = None
        self.right = None
        self.value = value      #Operational value
        self.down : Node = None

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left
        if type(left) is str:
            self.left = self.check_expression(left)

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right
        if type(right) is str:
            self.right = self.check_expression(right)

    def get_operator(self):
        return self.value

    def set_operator(self, value):
        self.value = value

    def check_expression(self, remainder):
        if (len(remainder) > 2): #check --, ++
            if remainder[0:2] in expression:    #expression on the left
                return (remainder[2:]).strip() + " " + expression[remainder[0:2]]
            elif remainder[-2:] in expression:  #expression on the right
                 return (remainder[:-2]).strip() + " " + expression[remainder[-2:]]
        return remainder

class CharNode:
    def __init__(self, value, parent):
        self.value = value
        self.next = None
        self.parent = parent
        self.is_variable = False

    #Next can be Node or CharNode or None
    def set_next(self, next):
        self.next = next

    def get_parent(self):
        return self.parent

class SyntaxTree:
    def __init__(self, raw_string : str):
        self.root = Node(None) #Root is always a node
        self.raw_string = self.to_python_keywords(raw_string)
        self.convert()

    def to_python_keywords(self, line : str):
        line = line.replace("true", "True")
        line = line.replace("false", "False")
        return line

    def convert(self):
        self.translate(self.raw_string.strip(), self.root)

    def translate(self, line : str, walk):
        remainder = ""
        for index, char in enumerate(line):
            if index == (len(line) - 1):  #Hits the last index
                if type(walk) is CharNode:
                    if char == ')':
                        new_node = CharNode(remainder.strip(), walk)
                        walk.set_next(new_node)
                    else:
                        new_node = CharNode(remainder.strip() + char, walk)
                        walk.set_next(new_node)
                else:
                    if char == ')':
                        walk.set_right(remainder.strip())
                    else:
                        walk.set_right(remainder.strip() + char)
                return
            elif char == ')': #Go up to next '('
                if type (walk) is CharNode and remainder != "":
                    new_node = CharNode(remainder.strip(), walk)
                    walk.set_next(new_node)
                if type(walk) is Node and remainder != "":
                    walk.set_right(remainder.strip())

                while walk.parent != None:
                    walk = walk.parent
                    if walk.value == "(":
                        break

                self.translate(line[(index + 1):].strip(), walk)
                return
            #On one operator character match
            elif char in conditional_single_operator:
                two_operator = line[index] + line[index + 1]
                if not(two_operator in conditional_operator):
                    two_operator = line[index]
                #Check two charactor operators first
                if two_operator in conditional_operator:
                    if type(walk) is CharNode:
                        if walk.next == None:
                            new_node = Node(conditional_operator[two_operator])
                            walk.set_next(new_node)
                            new_node.set_left(remainder.strip())
                            new_node.set_parent(walk)
                            self.translate(line[(index + 2):].strip(), new_node)
                            return
                        else:
                            if walk.parent == self.root: #Always node
                                walk.parent.set_operator(conditional_operator[two_operator])
                                self.translate(line[(index + 2):].strip(), walk.parent)
                                return

                            new_node = Node(conditional_operator[two_operator])
                            if type(walk) is CharNode:
                                walk.set_next(new_node)
                            else:
                                walk.set_left(new_node)
                            new_node.set_parent(walk)
                            new_node.set_left(remainder.strip())
                            self.translate(line[(index + 2):].strip(), new_node)
                            return
                    else:
                        if walk.left == None: #Normal case
                            walk.set_left(remainder.strip())
                            walk.set_operator(conditional_operator[two_operator])
                            self.translate(line[(index + 2):].strip(), walk) #Update parent
                            return
                        elif walk.right == None: #Right is empty
                            #Take right
                            new_child = Node(conditional_operator[two_operator])
                            new_child.set_left(remainder.strip())
                            new_child.set_parent(walk)
                            walk.set_right(new_child)
                            self.translate(line[(index + 2):].strip(), new_child) #Update parent
                            return
                        else: #Every children field is full
                            new_parent = Node(conditional_operator[two_operator])
                            if walk == self.root:
                                new_parent.set_left(walk)
                                walk.set_parent(new_parent)
                                self.root = new_parent
                                self.translate(line[(index + 2):].strip(), new_parent) #Update parent
                                return
                            else:
                                if type(walk.parent) is CharNode:
                                    walk.parent.set_next(new_parent)
                                else:
                                    walk.parent.set_left(new_parent)
                                new_parent.set_parent(walk.parent)
                                new_parent.set_left(walk)
                                walk.set_parent(new_parent)
                                self.translate(line[(index + 2):].strip(), new_parent) #Update parent
                                return

            if char in expression: #Detects '(', '!'
                if type(walk) is CharNode:
                    char_node = CharNode(expression[char], walk)
                    walk.set_next(char_node)
                    self.translate(line[(index + 1):].strip(), char_node)
                    return
                else:
                    if walk.left == None:   #Left
                        char_node = CharNode(expression[char], walk)
                        walk.set_left(char_node)
                        self.translate(line[(index + 1):].strip(), char_node)
                        return
                    else:                   #Right
                        char_node = CharNode(expression[char], walk)
                        walk.set_right(char_node)
                        self.translate(line[(index + 1):].strip(), char_node)
                        return
            remainder += char

    def get_conditional_script(self, walk, script : str):
        if type(walk) is Node:
            if type(walk.left) is str:
                script += walk.left
            else:
                script = self.get_conditional_script(walk.left, script)
            #check variables
            script += " " + str(walk.value) + " "
            if type(walk.right) is str:
                script += walk.right
            else:
                script = self.get_conditional_script(walk.right, script)
        elif type(walk) is CharNode: # CharNode type
            script += walk.value
            script = self.get_conditional_script(walk.next, script)
            return script + ")" if walk.value == "(" else script
        return script