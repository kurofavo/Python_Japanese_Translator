from translate import Translator
translator = Translator(to_lang="ja")
try:
    with open("filename", mode="r", encoding='utf-8') as my_file:
        new = my_file.read()
    translation = translator.translate(new)
    with open("newfiilename", mode="w", encoding='utf-8') as my_file2:
        my_file2.write(translation)
except FileNotFoundError:
    print("file could not be found")
except UnicodeEncodeError as err:
    print(f"hey watch out{err}")
