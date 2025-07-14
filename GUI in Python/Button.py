from tkinter import *
win = Tk()
win.title("Buttons in GUI")

Button(win,text="STOP",width= 25,command= win.destroy).pack()

mainloop()