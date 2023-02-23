from tkinter import *
import calendar

def showCal():
    new_gui = Tk()
    new_gui.title("Calendar")
    new_gui.geometry("500x600")
    new_gui.config(background="white")
    
    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    Label(new_gui,text = cal_content,font = "Consolas 10 bold").grid(row=5,column=1,padx=20)
    
    new_gui.mainloop()
    
if __name__=="__main__":
    gui = Tk()
    gui.config(background="white")
    gui.title("CALENDAR")
    gui.geometry('250x140')
    
    cal = Label(gui,text="Calendar",bg="dark gray",font=("times",28,'bold')).grid(row=1,column=1)
    year = Label(gui,text="Enter Year",bg="light green").grid(row=2,column=1)
    year_field = Entry(gui)
    
    Show = Button(gui,text="Show Calendar",fg="White",bg="Black",command=showCal).grid(row=4,column=1)
    Exit = Button(gui,text="Exit",fg="Red",bg="Black",command=exit).grid(row=5,column=1)
    
    year_field.grid(row=3,column=1)
    
    gui.mainloop()