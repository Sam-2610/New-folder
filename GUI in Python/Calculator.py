import tkinter

root = tkinter.Tk()
root.title("Simple Calculator")
root.configure(bg="#f0f0f0")  # Background color

# Entry Field
e1 = tkinter.Entry(root, width=25, borderwidth=5, font=("Arial", 16), bg="#e0f7fa", fg="#000")
e1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Functions
def button_click(number): # type: ignore
    current = e1.get()
    e1.delete(0, tkinter.END)
    e1.insert(0, current + str(number)) # type: ignore

def button_clear():
    e1.delete(0, tkinter.END)

def button_add():
    global fnum
    global math
    math = "addition"
    fnum = int(e1.get())
    e1.delete(0, tkinter.END)

def button_equal():
    second_number = int(e1.get())
    e1.delete(0, tkinter.END)
    if math == "addition":
        e1.insert(0, fnum + second_number) # type: ignore
    elif math == "substraction":
        e1.insert(0, fnum - second_number) # type: ignore
    elif math == "multiplication":
        e1.insert(0, fnum * second_number) # type: ignore
    elif math == "division":
        if second_number != 0:
            e1.insert(0, fnum / second_number) # type: ignore
        else:
            e1.insert(0, "Error")

def button_subtract():
    global fnum
    global math
    math = "substraction"
    fnum = int(e1.get())
    e1.delete(0, tkinter.END)

def button_multiply():
    global fnum
    global math
    math = "multiplication"
    fnum = int(e1.get())
    e1.delete(0, tkinter.END)

def button_divide():
    global fnum
    global math
    math = "division"
    fnum = int(e1.get())
    e1.delete(0, tkinter.END)

# Style dictionary
btn_style = {"padx": 40, "pady": 20, "bg": "#4caf50", "fg": "white", "font": ("Arial", 12, "bold")} # type: ignore
op_style = {"padx": 39, "pady": 20, "bg": "#f44336", "fg": "white", "font": ("Arial", 12, "bold")} # type: ignore

# Buttons
button1 = tkinter.Button(root, text="1", command=lambda: button_click(1), **btn_style) # type: ignore
button2 = tkinter.Button(root, text="2", command=lambda: button_click(2), **btn_style) # type: ignore
button3 = tkinter.Button(root, text="3", command=lambda: button_click(3), **btn_style) # type: ignore
button4 = tkinter.Button(root, text="4", command=lambda: button_click(4), **btn_style) # type: ignore
button5 = tkinter.Button(root, text="5", command=lambda: button_click(5), **btn_style) # type: ignore
button6 = tkinter.Button(root, text="6", command=lambda: button_click(6), **btn_style) # type: ignore
button7 = tkinter.Button(root, text="7", command=lambda: button_click(7), **btn_style) # type: ignore
button8 = tkinter.Button(root, text="8", command=lambda: button_click(8), **btn_style) # type: ignore
button9 = tkinter.Button(root, text="9", command=lambda: button_click(9), **btn_style) # type: ignore
button0 = tkinter.Button(root, text="0", command=lambda: button_click(0), **btn_style) # type: ignore

buttonadd = tkinter.Button(root, text="+", command=button_add, **op_style) # type: ignore
buttonequal = tkinter.Button(root, text="=", padx=91, pady=20, bg="#2196f3", fg="white",
                             font=("Arial", 12, "bold"), command=button_equal)
buttonclear = tkinter.Button(root, text="Clear", padx=79, pady=20, bg="#9c27b0", fg="white",
                             font=("Arial", 12, "bold"), command=button_clear)
buttonsubtract = tkinter.Button(root, text="-", command=button_subtract, **op_style) # type: ignore
buttonmultiply = tkinter.Button(root, text="*", command=button_multiply, **op_style) # type: ignore
buttondivide = tkinter.Button(root, text="/", command=button_divide, **op_style) # type: ignore

# Grid layout
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonclear.grid(row=4, column=1, columnspan=2)
buttonadd.grid(row=5, column=0)
buttonequal.grid(row=5, column=1, columnspan=2)

buttonsubtract.grid(row=6, column=0)
buttonmultiply.grid(row=6, column=1)
buttondivide.grid(row=6, column=2)

tkinter.mainloop()
