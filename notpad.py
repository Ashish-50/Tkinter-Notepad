import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog
import os 
from gtts import gTTS




root = tkinter.Tk()  # this make a root instance
root.title("Untitled - NotePad")





root.geometry('754x630') #creating dimension for our notpad 
root['background']="#f7e9fb"






#buttons Functions
def new_file():
    root.title("Untitled - NotePad")
    file=None
    entry.delete(1.0,END) #here argument is starting from index one to end
def quitapp():
    root.destroy() #this will destroy the main root window
def save_file():
    open_file = filedialog.asksaveasfile(mode='w',defaultextension='*.txt') #first argument is while saving we are wrting something into file so we use w mode and 2nd argument is extension which i only one txt
    if open_file is None:
        return
    text = str(entry.get(1.0,END)) #get method get all words from index one to end 
    open_file.write(text)
    open_file.close()
def clear():
    entry.delete(1.0,END)
def open_file():
    file = filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content = file.read()
        entry.insert(INSERT,content)
def about():
    showinfo("Notepad","This Notepad is made by Ashish") #2 argument firsst is title of prompt and 2nd is message
def audio():
    fh=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if fh is not None:
        content = fh.read()
    language='en'
    output=gTTS(text=content,lang=language,slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')







# creating buttons
b1=Button(root,text='New File',command=new_file)
b1.place(x=0,y=0)
b2=Button(root,text="Save File",command = save_file)
b2.place(x=55,y=0)
b4=Button(root,text="Open File",command = open_file)
b4.place(x=110,y=0)
b3=Button(root,text="Clear",command = clear)
b3.place(x=170,y=0)
b6=Button(root,text="About",command= about)
b6.place(x=207,y=0)
b7=Button(root,text="Text To Audio",command=audio)
b7.place(x=250,y=0)
b5=Button(root,text="Quit",command=quitapp)
b5.place(x=330,y=0)


# creating text file
entry = Text(root,height=26,width=74,wrap=WORD,font="Times")
# entry = Text(root,wrap=WORD,font="Times")
# entry.pack(fill=BOTH,expand=True)
entry.place(x=5,y=30)










root.mainloop()

