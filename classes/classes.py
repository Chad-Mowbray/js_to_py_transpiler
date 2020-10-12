import re
from .data import Data

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
        print(self.token_list)
        
    def process_token_list(self, recurse_list=None):
        tokens = recurse_list if recurse_list else self.token_list

        for token in tokens:
            if token.startswith(self.data.comment): break

            if token == self.data.function_keyword: self.process_function(self.token_list); break

            is_for = re.search(self.data.for_operator, token)
            if is_for: self.process_for(self.token_list); break

            is_method = re.search(self.data.method_indicator, token)
            if is_method: self.process_method(token); continue

            if token in self.data.variable_declarations: continue

            variable = re.search(self.data.variable, token) 
            if variable: self.translated.append(token); continue 

            if token in self.data.assignment: self.translated.append(token); continue

            is_integer = re.search(self.data.integer, token)
            if is_integer: self.translated.append(token); continue

            if token in self.data.math_operators: self.translated.append(token); continue
    
    def process_method(self, token):
        if not re.search(r'[.]', token): self.process_function_call(token)
        else: 
            split_token = token.split('(')
            before_parens, after_parens = split_token[0], "(" + split_token[1]
            if before_parens in self.data.built_ins:
                self.translated.append(self.data.built_ins[before_parens] + after_parens)
            else: raise Exception("not a built-in")

    def process_function(self, token_list):
        self.translated.append("def")
        self.translated.append(token_list[1] + ":")
        self.translated.append("\n\t")
        self.token_list = token_list[3:-1]
        self.process_token_list()
    
    def process_function_call(self, token):
        self.translated.append(token)

    def process_for(self, token_list):
        var_name = token_list[1]
        start = token_list[3][:-1]
        stop = token_list[6][:-1]
        step = token_list[7][:-1]

        is_plusplus = re.search(self.data.plus_plus, step)
        if is_plusplus: step = "1"
        else: step = token_list[9][:-1]

        for_init = f"for {var_name} in range({start},{stop},{step}):\n\t"
        self.translated.append(for_init)

        start =token_list.index("{")
        self.process_for_body(token_list[start + 1:-1])
    
    def process_for_body(self, body_list):
        self.process_token_list(body_list)


    def get_translation(self):
        self.process_token_list()
        translated_string = " ".join(self.translated)
        return translated_string




