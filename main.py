from classes.classes import Tokenizer, Translator
from file_io import FileIO

def main():
    contents = FileIO().read_js_file()
    translated = []

    for line in contents:
        line_tokens = Tokenizer(line).elements
        translation = Translator(line_tokens)
        translated.append(translation.get_translation())

    FileIO().write_py_file(translated)

if __name__ == "__main__":
    main()
