from tkinter import *

def submit_form():
    print("---- Submitted Data ----")
    print("First Name:", e1.get())
    print("Second Name:", e2.get())
    print("Class:", e3.get())
    print("School Name:", e4.get())

    gender = var1.get()
    print("Gender:", "Male" if gender == 1 else "Female" if gender == 2 else "Not selected")

    subjects = []
    if v1.get(): subjects.append("English")
    if v2.get(): subjects.append("Maths")
    if v3.get(): subjects.append("Science")
    if v4.get(): subjects.append("Computer Science")
    print("Subjects Chosen:", ", ".join(subjects) if subjects else "None")

def reset_form():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    var1.set(0)
    v1.set(0)
    v2.set(0)
    v3.set(0)
    v4.set(0)

win = Tk()
win.title("College Admission Form")

Label(win, text="COLLEGE ADMISSION FORM", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

Label(win, text="First Name").grid(row=1, column=0, sticky=W)
Label(win, text="Second Name").grid(row=2, column=0, sticky=W)
Label(win, text="Class").grid(row=3, column=0, sticky=W)
Label(win, text="School Name").grid(row=4, column=0, sticky=W)

e1 = Entry(win)
e2 = Entry(win)
e3 = Entry(win)
e4 = Entry(win)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)

Label(win, text="CHOOSE YOUR GENDER...").grid(row=5, column=0, sticky=W, pady=10)
var1 = IntVar()
Radiobutton(win, text="Male", variable=var1, value=1).grid(row=6, column=0, sticky=W)
Radiobutton(win, text="Female", variable=var1, value=2).grid(row=6, column=1, sticky=W)

Label(win, text="CHOOSE YOUR SUBJECTS...").grid(row=7, column=0, sticky=W, pady=10)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
Checkbutton(win, text="English", variable=v1).grid(row=8, column=0, sticky=W)
Checkbutton(win, text="Maths", variable=v2).grid(row=9, column=0, sticky=W)
Checkbutton(win, text="Science", variable=v3).grid(row=10, column=0, sticky=W)
Checkbutton(win, text="Computer Science", variable=v4).grid(row=11, column=0, sticky=W)

Button(win, text="Submit", width=25, command=submit_form).grid(row=12, column=0, pady=10)
Button(win, text="Reset", width=25, command=reset_form).grid(row=12, column=1, pady=10)

win.mainloop()
