from classes.classes import Tokenizer, Translator

contents = ''
translated = []

with open('origin_files/js.js') as js_file:
    contents = js_file.readlines()

for line in contents:
    line_tokens = Tokenizer(line).elements
    translation = Translator(line_tokens)
    translated.append(translation.get_translation())

with open('translated_files/pythonified.py', 'w') as translation:
    for line in translated:
        line = line.replace("\t ", "\t") 
        translation.write(f"{line}\n")
