import pyttsx3 
import PyPDF2

#PDF location
path = open('/home/anonimouz/Documents/python projects/content/ai.pdf','rb')
pdf = PyPDF2.PdfReader(path) #Scans through pdf
page = pdf.pages[20] #selects the page
txt = page.extract_text() #extract the content

print(txt)

#Outputs as speech
engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()
