import re


class Data:  # singleton

    variable_declarations = ["var", "let", "const"]
    assignment = ["="]
    integer = r'[0-9]+'
    variable = r'[a-zA-z0-9]+'
    built_ins = {
        "console.log": "print"
    }
    method_indicator = r'[.()]'

    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance



class Tokenizer:

    def __init__(self, line):
        self.line = line
        self.elements = self.line.split(' ')

    def __str__(self):
        return f"""Tokenizer({self.line})
        elements: {self.elements}"""

    def __repr__(self):
        return f"Tokenizer({self.line})"


class Translator:

    def __init__(self, token_list):
        self.data = Data()
        self.token_list = [t.replace("\n", "") for t in token_list]
        self.translated = []
        
    def process_token_list(self):
        for token in self.token_list:
            is_method = re.search(self.data.method_indicator, token)
            if is_method: self.process_method(token); continue
            if token in self.data.variable_declarations: continue
            variable = re.search(self.data.variable, token) 
            if variable: self.translated.append(token); continue 
            if token in self.data.assignment: self.translated.append(token); continue
    
    def process_method(self, token):
        split_token = token.split('(')
        before_parens, after_parens = split_token[0], "(" + split_token[1]
        if before_parens in self.data.built_ins:
            self.translated.append(self.data.built_ins[before_parens] + after_parens)
        else: raise Exception("not a built-in")


    def get_translation(self):
        self.process_token_list()
        return " ".join(self.translated)



