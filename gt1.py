from googletrans import Translator,LANGUAGES
trans=Translator()
print("the available supported languages are")
for i,l in LANGUAGES.items():
    print(f"{i}: {l}")
text=input("enter text to translate")
lang=input("enter the source language")
tlang=input("enter the target language")
lang=trans.detect(text).lang
ttext=trans.translate(text,src=lang,dest=tlang)
print(f"translated text: {ttext.text}")

