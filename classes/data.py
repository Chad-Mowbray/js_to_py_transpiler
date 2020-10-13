import re

class Data:

    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    variable_declarations = ["var", "let", "const"]
    assignment = ["="]
    integer = r'[0-9]+'
    variable = r'^[^0-9{][a-zA-z0-9]*'
    built_ins = {
        "console.log": "print"
    }
    method_indicator = r'[.](?=.+\()' 
    function_keyword = "function"
    open_bracket = "{"
    comment = "//"
    math_operators = ["+", "-", "*", "/"]
    for_operator = r'^for'
    plus_plus = r'\+\+$'
    list_bracket = r'^['
    length = r'.length$'
    colon = ":"
    object_property = f'{variable}[.][a-zA-z0-9]+$'

