from tkinter import *
from textblob import TextBlob

def clear_All():
    word1_f.delete(0,END)
    word2_f.delete(0,END)

def correction():
    input_word = word1_f.get()
    blob_obj = TextBlob(input_word)
    corrected_word = str(blob_obj.correct())
    word2_f.insert(10,corrected_word)
    
if __name__ == "__main__":
    root = Tk()
    root.title("Spell Corrector")
    root.configure(background="light gray")
    root.geometry("400x150")
    
    headLabel = Label(root,text="Welcome to spell checker",fg="black",bg="white")
    label1 = Label(root,text = "Input Word",fg="black",bg="white")
    label2 = Label(root,text = "Corrected Word",fg="black",bg="white")
    
    headLabel.grid(row=0,column=1)
    label1.grid(row=1,column=0)
    label2.grid(row=3,column=0)
    
    word1_f = Entry()
    word2_f = Entry()
    
    word1_f.grid(row=1,column=1,padx=10,pady=10)
    word2_f.grid(row=3,column=1,padx=10,pady=10)
    
    button1 = Button(root, text="Generate",bg="red",fg="black",command = correction)
    button1.grid(row=2,column=1)
    
    button2 = Button(root,text="Clear",bg="red",fg="black",command = clear_All)
    button2.grid(row=4,column=1)
    
    root.mainloop()
    
