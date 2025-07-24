from tkinter import * # type: ignore
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")

my_img1 = ImageTk.PhotoImage(Image.open("images/1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.png"))

from typing import List

image_list: List[ImageTk.PhotoImage] = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(root, image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

button_forward = Button(root, text=">>", command=lambda: forward(img_num + 1))
button_back = Button(root, text="<<", command=lambda: back(img_num - 1))

if img_num == 5:
    button_forward = Button(root,text=">>",state=DISABLED)

button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2)



def forward(img_num): # type: ignore
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    if isinstance(image_list[img_num - 1], ImageTk.PhotoImage):
        my_label = Label(root, image=image_list[img_num - 1])
    else:
        raise TypeError("Item at index {} in image_list is not a PhotoImage.".format(img_num - 1))
    my_label.grid(row=0,column=0,columnspan=3)


def back():
    global my_label
    global button_forward
    global button_back




button_back = Button(root,text="<<",command=back)
button_exit = Button(root,text="Exit Programme",command=root.quit)
button_forward = Button(root,text=">>",command= lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)



root.mainloop()