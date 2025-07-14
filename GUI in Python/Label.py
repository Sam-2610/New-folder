import tkinter                # Import the tkinter module
win = tkinter.Tk()            # Create the main window
win.title("Label in GUI")     # Set the window title

l1 = tkinter.Label(win, text="Hello!")  # Create a Label widget with the text "Hello!"
l1.pack()                    # Place the label in the window using the pack layout manager

win.mainloop()               # Start the GUI event loop
