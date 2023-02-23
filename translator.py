from translate import Translator 
lang = input("Enter The Language : ")
text = input("Enter The Text : ")
a = Translator(to_lang=lang)
b = a.translate(text)
print(b)