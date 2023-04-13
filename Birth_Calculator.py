import tkinter as tk
from tkinter import messagebox
import datetime
from PIL import Image, ImageTk
window = tk.Tk()
window.geometry("220x180")
window.title("Age Calculator")
name = tk.Label(text = "Name")
name.grid(column = 3 , row = 1)
month = tk.Label(text = "month")
month.grid(column = 3 , row = 3)
year  = tk.Label(text = "year ")
year.grid(column = 3 , row = 5)
Date = tk.Label(text = "Date")
Date.grid(column = 3 , row = 7)
NameEntry = tk.Entry()
NameEntry.grid(column = 5 , row =1)
monthEntry = tk.Entry()
monthEntry.grid(column = 5 , row =3)
yearEntry = tk.Entry()
yearEntry.grid(column = 5, row =5)
dateEntry = tk.Entry()
dateEntry.grid(column = 5 , row =7)
def getInput():
    name = NameEntry.get()
    key = Person(name , datetime.date(int(yearEntry.get()),
                                      int(monthEntry.get()),
                                      int(dateEntry.get())))

    textArea =tk.Text(master =window ,height = 10 , width = 25)
    # textArea.grid(column = 12, row = 11)
    answer = " Hey {key} you are {age} years old .".format(key = name , age = key.age())
    messagebox.showinfo(f"{name}",f"{answer}")

    textArea.insert(tk.END , answer)


button = tk.Button(window , text = "Calculate age ",command = getInput ,bg = "red")
button.grid(column = 5 , row = 10)





class Person :
    def __init__(self , name , birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
    def days(self):
        today = datetime.date.today()
        days= today.year-self.birthdate.year
        return days


window.mainloop()

