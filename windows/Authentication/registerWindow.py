import tkinter as tk
from tkinter import messagebox, Canvas, NW
from PIL import ImageTk, Image
from models.users import register, get_logged_user, checkUnique
from styles.colors import *
from styles.fonts import *
from widgets.widgets import Button, Input
from windows.Home import homeWindow
from utils import checkEmail, togglePasswordVisibility, manageVisibility, checkUsername

# global variable
isRegister = (
    False  # this variable will be used to check if the user is registering or not
)


def register(Window: object) -> None:
    """
    This function is used to create the regsiter window.

    :param Window: The window of the application.

    :return: None
    """

    # open the window
    registerWindow = tk.Toplevel()

    # centering the window
    registerWindowWidth = 590  # width of the window
    registerWindowHeight = 670  # height of the window

    screenWidth = registerWindow.winfo_screenwidth()  # width of the screen

    screenHeight = registerWindow.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (registerWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (registerWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    registerWindow.geometry(
        "%dx%d+%d+%d" % (registerWindowWidth, registerWindowHeight, x, y)
    )
    registerWindow.title("Login")
    registerWindow.iconbitmap("assets/PhotoShowIcon.ico")
    registerWindow.resizable(0, 0)
    registerWindow.config(bg=colors["primary-50"])

    canvasLogo = Canvas(registerWindow, height=120, width=334, highlightthickness=0)
    canvasLogo.place(x=125, y=20)

    logo_image = Image.open("assets/images/Logo_auth.png")
    logo_image = logo_image.resize((334, 120))

    canvasLogo.image = ImageTk.PhotoImage(logo_image)

    canvasLogo.create_image(0, 0, anchor=NW, image=canvasLogo.image)

    # ---------------------------

    # email icon label
    emailIcon = Image.open("assets/images/UI_Icons/Email_Icon.png")
    emailIcon = emailIcon.resize((48, 44))

    canvasEmailIcon = Canvas(registerWindow, height=40, width=46, highlightthickness=0)
    canvasEmailIcon.place(x=130, y=170)

    canvasEmailIcon.image = ImageTk.PhotoImage(emailIcon)

    canvasEmailIcon.create_image(0, 0, anchor=NW, image=canvasEmailIcon.image)

    # ---------------------------

    # username icon label
    usernameIcon = Image.open("assets/images/UI_Icons/Username_Icon.png")
    usernameIcon = usernameIcon.resize((48, 44))

    canvasUsernameIcon = Canvas(
        registerWindow, height=40, width=46, highlightthickness=0
    )
    canvasUsernameIcon.place(x=130, y=280)

    canvasUsernameIcon.image = ImageTk.PhotoImage(usernameIcon)
    canvasUsernameIcon.create_image(0, 0, anchor=NW, image=canvasUsernameIcon.image)

    # ---------------------------

    # email label
    emailLabel = tk.Label(
        registerWindow,
        text="email",
        font=quickSandBold(14),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )
    emailLabel.place(x=175, y=190, anchor="w")

    # ---------------------------

    # username label
    usernameLabel = tk.Label(
        registerWindow,
        text="username",
        font=quickSandBold(14),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )
    usernameLabel.place(x=175, y=302, anchor="w")

    # ---------------------------

    # Input email
    Input(
        registerWindow,
        width=30,
        borderwidth=0,
        fontSize=12,
        placeX=140,
        placeY=220,
    )

    # ---------------------------

    # Input username
    Input(
        registerWindow,
        width=30,
        borderwidth=0,
        fontSize=12,
        placeX=140,
        placeY=330,
    )

    registerWindow.mainloop()
