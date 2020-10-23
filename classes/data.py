import re
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Data:

    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    variable_declarations: list = field(default_factory=lambda: ["var", "let", "const"])
    assignment: list = field(default_factory=lambda: ["="])
    integer: str = r'[0-9]+'
    variable: str = r'^[^0-9{][a-zA-z0-9]*'
    built_ins: object = field(default_factory=lambda: {"console.log": "print"})
    method_indicator: str = r'[.](?=.+\()' 
    function_keyword: str = "function"
    open_bracket: str = "{"
    comment: str = "//"
    math_operators: list = field(default_factory=lambda: ["+", "-", "*", "/"])
    for_operator: str = r'^for'
    plus_plus: str = r'\+\+$'
    list_bracket: str = r'^['
    length: str = r'.length$'
    colon: str = ":"
    object_property: str = f'{variable}[.][a-zA-z0-9]+$'
