from tkinter import *
from PIL import ImageTk, Image

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
mainImage = ImageTk.PhotoImage(Image.open("assets/images/Home_background.png"))

# to insert the image on the canvas
mainCanvas.create_image(0, 0, anchor=NW, image=mainImage)

# to insert the canvas on the window with pack method
mainCanvas.pack()


Window.mainloop()