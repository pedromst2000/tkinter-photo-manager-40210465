from tkinter import *
from PIL import ImageTk, Image
from widgets.Button import _Button_
from styles.colors import *
from styles.fonts import *
from windows.Authentication.loginWindow import login
from widgets.Input import _Input_

Window = Tk()

Window.title("PhotoShow")
Window.geometry("1350x700")

# to insert the icon on the window
Window.iconbitmap("assets/PhotoShowIcon.ico")

# remove the maximize button
Window.resizable(0, 0)


# canvas
mainCanvas = Canvas(Window, width=1350, height=700)
mainCanvas.place(x=0, y=0)

mainImage = Image.open("assets/images/main_background.png")
mainImage = mainImage.resize((1350, 700))

mainImage = ImageTk.PhotoImage(mainImage)

mainCanvas.create_image(0, 0, image=mainImage, anchor=NW)


logoImage = Image.open("assets/images/Logo.png")
logoImage = logoImage.resize((600, 200))

logoImage = ImageTk.PhotoImage(logoImage)

mainCanvas.create_image(390, 50, image=logoImage, anchor=NW)

sloganText = mainCanvas.create_text(
    550,
    300,
    text="Every Pixel Tells a Tale",
    font=(quickSandBold(25)),
    fill=colors["accent-500"],
    anchor=NW,
)

# Button Widget
_Button_(
    width=18,
    height=2,
    text="Sign In",
    fontSize=16,
    window=mainCanvas,
    placeX=600,
    placeY=500,
    event=lambda event: login(Window),
)


Window.mainloop()
