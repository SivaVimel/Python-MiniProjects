import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate',175)
    
    engine.say(audio)
    engine.runAndWait()

text = input("Enter The Text : ")    
speak(text)