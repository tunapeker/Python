from tkinter import *
from PIL import Image,ImageTk

root = Tk()

root.title("Image Viewer")
root.iconbitmap("images/icons/camera.ico")

img1 = ImageTk.PhotoImage(Image.open("URL1"))
img2 = ImageTk.PhotoImage(Image.open("URL2"))
img3 = ImageTk.PhotoImage(Image.open("URL3"))
img4 = ImageTk.PhotoImage(Image.open("URL4"))
img5 = ImageTk.PhotoImage(Image.open("URL5"))

image_list=[img1,img2,img3,img4,img5]


label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)

status= Label(root, text="Image 1 of {}".format(len(image_list)), bd=1,relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global label
    global button_back
    global button_forward

    label.grid_forget()
    label = Label(image=image_list[image_number - 1])
    label.grid(row=0, column=0, columnspan=3)

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_forward.grid(row=1, column=2)

    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_back.grid(row=1, column=0)

    if image_number == 1:
        button_back = Button(root, text="<<", command=lambda: back(image_number - 1), state=DISABLED)
        button_back.grid(row=1, column=0)
    status = Label(root, text="Image {} of {}".format(image_number,len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def forward(image_number):
    global label
    global button_back
    global button_forward

    label.grid_forget()
    label = Label(image=image_list[image_number-1])
    label.grid(row=0, column=0, columnspan=3)

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_forward.grid(row=1, column=2)

    if image_number == len(image_list):
        button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1), state=DISABLED)
        button_forward.grid(row=1, column=2)

    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_back.grid(row=1, column=0)

    status = Label(root, text="Image {} of {}".format(image_number, len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back = Button(root, text="<<", command=lambda: back(1))
button_back.grid(row=1, column=0)

button_exit = Button(root, text="Exit", command=root.quit)
button_exit.grid(row=1, column=1, pady=10)

button_forward = Button(root, text=">>", command=lambda: forward(2))
button_forward.grid(row=1, column=2)


root.mainloop()
