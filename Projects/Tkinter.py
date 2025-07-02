import tkinter as tk

window = tk.Tk()
window.title("Simple GUI")
window.geometry('350x200')

l1 = tk.Label(window,text="Hello")
l1.grid(column=0,row=0)

window.mainloop()



 