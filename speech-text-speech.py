import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
def speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
while(1):
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source, phrase_time_limit=3)
        myText = r.recognize_google(audio, language='en')
        myText = myText.lower()
        print("You Said ",myText)
        speak(myText)