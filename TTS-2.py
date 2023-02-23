from gtts import gTTS 
from playsound import playsound
a = input("Enter The Text : ")
tts = gTTS(text=a,lang="en")
tts.save('/home/anonimouz/Documents/python projects/content/test.mp3')
playsound('/home/anonimouz/Documents/python projects/content/test.mp3')