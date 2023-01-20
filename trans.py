from translate import Translator
translator = Translator(to_lang="ja")
try:
	with open("test.txt", mode="r", encoding='utf-8') as my_file:
	    lll = my_file.read()
	translation = translator.translate(lll)
	with open("lol.txt", mode="w", encoding='utf-8') as my_file2:
		my_file2.write(translation)
except FileNotFoundError:
	print("file could not be found")
except UnicodeEncodeError as err:
	print(f"hey watch out{err}")