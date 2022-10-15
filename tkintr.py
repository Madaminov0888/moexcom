from tkinter import*
#import os, fnmatch
import datetime
from tkcalendar import DateEntry

def submitForm():    
    strFile = cal.get()
    satr2 = cal2.get()
    # Print the selected value from Option (Combo Box)    
    if (strFile !=''):   
        root.destroy()     
        print([strFile, satr2])



root = Tk()
root.geometry('500x500')
root.title("Dogovor ")

cal2 = DateEntry(root, width=12, year=2019, month=6, day=22, 
background='blue', foreground='white', borderwidth=6)


cal = DateEntry(root, width=12, year=2019, month=6, day=22, 
background='blue', foreground='white', borderwidth=6)
cal.pack(padx=10, pady=40)
cal2.pack(padx=10, pady=40)




label_2 = Label(root, text="Choose dates ",width=40,font=("bold", 10))
label_2.place(x=60,y=10)

label1 = Label(root,text="From:",width=10,font=("bold", 10))
label1.place(x=110,y=40)

label1 = Label(root,text="To:",width=10,font=("bold", 10))
label1.place(x=110,y=150)


"""
optVariable = StringVar(root)
optVariable.set("   Select start date   ") # default value
optFiles = OptionMenu(root, optVariable, *flist)
optFiles.pack()
optFiles.place(x=150,y=20)
"""

Button(root, text='Submit', command=submitForm, width=20,bg='brown',fg='white').place(x=180,y=180)


root.mainloop()
