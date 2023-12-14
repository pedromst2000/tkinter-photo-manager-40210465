import tkinter
import tkinter.font
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
from styles.colors import *


Window = Tk()

Window.title("PhotoShow")
Window.geometry("1350x700")

# to insert the icon on the window
Window.iconbitmap("assets/PhotoShowIcon.ico")

# remove the maximize button
Window.resizable(0, 0)

# Todo => Text Fonts 

# # canvas
mainCanvas = Canvas(Window, width=1350, height=700)

# # to insert the image on the canvas
mainImage = ImageTk.PhotoImage(Image.open("assets/images/Home_background.png"))

# to insert the image on the canvas
mainCanvas.create_image(0, 0, anchor=NW, image=mainImage)


square = mainCanvas.create_rectangle(0, 0, 1350, 700, fill=colors["secondary-300"])

# insert the square on the canvas
mainCanvas.place(x=0, y=0)


Window.mainloop()
