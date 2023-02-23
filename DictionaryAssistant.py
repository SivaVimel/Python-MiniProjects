from gtts import gTTS 
from playsound import playsound 
from PyDictionary import PyDictionary

tts = gTTS(text="Enter The Text",lang = 'en')
tts.save('/home/anonimouz/Documents/python projects/content/first.mp3')
playsound('/home/anonimouz/Documents/python projects/content/first.mp3')
text = input("Enter The Word : ")
dic = PyDictionary()
word = dic.meaning(text)

for m in word:
    a = word[m]
    
    for i in a:
        print(i)
        tts = gTTS(text = text+' is a '+i,lang='en')
        tts.save('/home/anonimouz/Documents/python projects/content/meaning.mp3')
        playsound('/home/anonimouz/Documents/python projects/content/meaning.mp3')
        