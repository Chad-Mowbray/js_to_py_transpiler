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
    function_keyword = "function"
    open_bracket = "{"

    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

