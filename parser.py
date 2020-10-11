from classes import Tokenizer, Translator

contents = ''
translated = []

with open('js.js') as js_file:
    contents = js_file.readlines()

for line in contents:
    line_tokens = Tokenizer(line).elements
    translation = Translator(line_tokens)
    translated.append(translation.get_translation())

with open('pythonified.py', 'w') as translation:
    for line in translated:
        translation.write(f"{line}\n")
