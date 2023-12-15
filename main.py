from tkinter import *
from PIL import ImageTk, Image
from widgets.Button import _Button_

Window = Tk()

Window.title("PhotoShow")
Window.geometry("1350x700")

# to insert the icon on the window
Window.iconbitmap("assets/PhotoShowIcon.ico")

# remove the maximize button
Window.resizable(0, 0)


# canvas
mainCanvas = Canvas(Window, width=1350, height=700)

# to insert the image on the canvas
mainImage = ImageTk.PhotoImage(Image.open("assets/images/main_background.png"))

mainCanvas.create_image(0, 0, anchor=NW, image=mainImage)

logoImage = ImageTk.PhotoImage(Image.open("assets/images/Logo.png"))
logoImage = logoImage.resize((300, 300), Image.ANTIALIAS)


mainCanvas.create_image(0, 0, anchor=NW, image=logoImage)

# Button Widget
_Button_(
    width=18,
    height=2,
    text="Sign In",
    fontSize=16,
    window=mainCanvas,
    placeX=600,
    placeY=500,
)


mainCanvas.pack()

Window.mainloop()
