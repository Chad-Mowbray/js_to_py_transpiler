
class FileIO:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    @staticmethod
    def read_js_file():
        contents = None
        with open('origin_files/js.js') as js_file:
            contents = js_file.readlines()
        return contents

    def write_py_file(self, translated):
        with open('translated_files/pythonified.py', 'w') as translation:
            for line in translated:
                line = line.replace("\t ", "\t") 
                translation.write(f"{line}\n")