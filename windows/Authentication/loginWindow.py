import tkinter as tk
from tkinter import messagebox, Canvas, NW, Button, Entry
from PIL import ImageTk, Image
from models.users import login, checkLoggedUserRole, checkLoggedUserIsBlocked
from styles.colors import *
from widgets.Input import _Input_

# global variable
isLogged = False  # this variable will be used to check if the user is logged or not
isRegister = (
    False  # this variable will be used to check if the user is registering or not
)


def login(Window: object) -> None:
    """
    This function is used to create the login window.

    :param Window: The window of the application.

    :return: None
    """

    # open the window
    loginWindow = tk.Toplevel()

    # centering the window
    loginWindowWidth = 573  # width of the window
    loginWindowHeight = 580  # height of the window

    screenWidth = loginWindow.winfo_screenwidth()  # width of the screen

    screenHeight = loginWindow.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (loginWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (loginWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    loginWindow.geometry("%dx%d+%d+%d" % (loginWindowWidth, loginWindowHeight, x, y))
    loginWindow.title("Login")
    loginWindow.iconbitmap("assets/PhotoShowIcon.ico")
    loginWindow.resizable(0, 0)
    loginWindow.config(bg=colors["primary-50"])

    canvasLogo = Canvas(loginWindow, height=120, width=334, highlightthickness=0)
    canvasLogo.place(x=120, y=20)

    logo_image = Image.open("assets/images/Logo_auth.png")
    logo_image = logo_image.resize((334, 120))

    canvasLogo.image = ImageTk.PhotoImage(logo_image)

    canvasLogo.create_image(0, 0, anchor=NW, image=canvasLogo.image)

    # email icon label
    emailIcon = Image.open("assets/images/UI_Icons/Email_Icon.png")
    emailIcon = emailIcon.resize((22, 20))

    canvasEmailIcon = Canvas(loginWindow, height=20, width=22, highlightthickness=0)
    canvasEmailIcon.place(x=120, y=180)

    canvasEmailIcon.image = ImageTk.PhotoImage(emailIcon)

    canvasEmailIcon.create_image(0, 0, anchor=NW, image=canvasEmailIcon.image)

    # _Input_(
    #     width=30,
    #     borderwidth=0,
    #     fontSize=12,
    #     placeX=120,
    #     placeY=220,
    # )
  
       
    
    
    
    loginWindow.mainloop()