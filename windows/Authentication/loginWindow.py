import tkinter as tk
from tkinter import messagebox, Canvas, NW
from PIL import ImageTk, Image
from models.users import login, get_logged_user
from styles.colors import *
from styles.fonts import *
from widgets.widgets import Button, Input
from windows.Home import homeWindow
from utils import checkEmail, togglePasswordVisibility, manageVisibility, checkUsername

# global variable
isLogged = False  # this variable will be used to check if the user is logged or not


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
    canvasLogo.place(x=125, y=20)

    logo_image = Image.open("assets/images/Logo_auth.png")
    logo_image = logo_image.resize((334, 120))

    canvasLogo.image = ImageTk.PhotoImage(logo_image)

    canvasLogo.create_image(0, 0, anchor=NW, image=canvasLogo.image)

    # ---------------------------

    # email icon label
    emailIcon = Image.open("assets/images/UI_Icons/Email_Icon.png")
    emailIcon = emailIcon.resize((48, 44))

    canvasEmailIcon = Canvas(loginWindow, height=40, width=46, highlightthickness=0)
    canvasEmailIcon.place(x=130, y=170)

    canvasEmailIcon.image = ImageTk.PhotoImage(emailIcon)

    canvasEmailIcon.create_image(0, 0, anchor=NW, image=canvasEmailIcon.image)

    # ---------------------------

    # password icon label
    passwordIcon = Image.open("assets/images/UI_Icons/Password_Icon.png")
    passwordIcon = passwordIcon.resize((48, 44))

    canvasPasswordIcon = Canvas(loginWindow, height=40, width=46, highlightthickness=0)
    canvasPasswordIcon.place(x=130, y=280)

    canvasPasswordIcon.image = ImageTk.PhotoImage(passwordIcon)
    canvasPasswordIcon.create_image(0, 0, anchor=NW, image=canvasPasswordIcon.image)

    # ---------------------------

    # manage password
    canvasManagePassword = Canvas(
        loginWindow, height=26, width=40, highlightthickness=0, cursor="hand2"
    )

    canvasManagePassword.config(highlightthickness=0, bd=0, bg=colors["primary-50"])

    # email label
    emailLabel = tk.Label(
        loginWindow,
        text="email",
        font=quickSandBold(14),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )
    emailLabel.place(x=175, y=190, anchor="w")

    # ---------------------------

    # password label
    passwordLabel = tk.Label(
        loginWindow,
        text="password",
        font=quickSandBold(14),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )
    passwordLabel.place(x=175, y=302, anchor="w")

    # ---------------------------
    Input(
        loginWindow,
        width=30,
        borderwidth=0,
        fontSize=12,
        placeX=140,
        placeY=220,
        inputType="email",
    )

    # ---------------------------
    Input(
        loginWindow,
        width=30,
        borderwidth=0,
        fontSize=12,
        placeX=140,
        placeY=330,
        inputType="password",
    )

    loginWindow.mainloop()
