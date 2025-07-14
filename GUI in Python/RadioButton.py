from tkinter import *
win = Tk()
win.title("RadioButton in GUI")

var1 = IntVar()

Radiobutton(win,text= "IIT",variable= var1,value=1).pack(anchor=W)



Radiobutton(win,text= "MIT",variable= var1,value=2).pack(anchor=W)

mainloop()