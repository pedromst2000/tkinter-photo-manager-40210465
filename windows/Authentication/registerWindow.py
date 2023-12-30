import tkinter as tk
from tkinter import messagebox, Canvas, Label, Entry, Button, NW
from PIL import ImageTk, Image
from models.users import register, checkSignUpEmail, checkSignUpUsername, getUserInfo
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from windows.Home.homeWindow import homeWindow
from utils.widgets.input import on_focus_in, on_focus_out, on_click_outside
from utils.widgets.button import (
    on_enter as button_on_enter,
    on_leave as button_on_leave,
)
from utils.authentication.authentication import (
    checkEmail,
    checkUsername,
    togglePasswordVisibility,
    manageVisibility,
    on_enter as label_on_enter,
    on_leave as label_on_leave,
)

# global variable flags
isLogged = False  # this variable will be used to check if the user is logged or not
isNewUser = False  # this variable will be used to check if the user is new or not


def registerWindow(Window: object) -> None:
    """
    This function is used to create the register window.

    :param Window: The window of the application.

    :return: None
    """

    # open the window
    _registerWindow_ = tk.Toplevel()

    # centering the window
    registerWindowWidth = 590  # width of the window
    registerWindowHeight = 670  # height of the window

    screenWidth = _registerWindow_.winfo_screenwidth()  # width of the screen

    screenHeight = _registerWindow_.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (registerWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (registerWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    _registerWindow_.geometry(
        "%dx%d+%d+%d" % (registerWindowWidth, registerWindowHeight, x, y)
    )
    _registerWindow_.title("Sign Up")
    _registerWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _registerWindow_.resizable(0, 0)
    _registerWindow_.config(bg=colors["primary-50"])

    canvasLogo = Canvas(_registerWindow_, height=120, width=334, highlightthickness=0)
    canvasLogo.place(x=120, y=20)

    logo_image = Image.open("assets/images/Logo_auth.png")
    logo_image = logo_image.resize((334, 120))

    canvasLogo.image = ImageTk.PhotoImage(logo_image)

    canvasLogo.create_image(0, 0, anchor=NW, image=canvasLogo.image)

    # ---------------------------

    # email icon label
    emailIcon = Image.open("assets/images/UI_Icons/Email_Icon.png")
    emailIcon = emailIcon.resize((48, 44))

    canvasEmailIcon = Canvas(
        _registerWindow_, height=40, width=46, highlightthickness=0
    )
    canvasEmailIcon.place(x=130, y=170)

    canvasEmailIcon.image = ImageTk.PhotoImage(emailIcon)

    canvasEmailIcon.create_image(0, 0, anchor=NW, image=canvasEmailIcon.image)

    # ---------------------------

    # password icon label
    passwordIcon = Image.open("assets/images/UI_Icons/Password_Icon.png")
    passwordIcon = passwordIcon.resize((48, 44))

    canvasPasswordIcon = Canvas(
        _registerWindow_, height=40, width=46, highlightthickness=0
    )
    canvasPasswordIcon.place(x=130, y=280)

    canvasPasswordIcon.image = ImageTk.PhotoImage(passwordIcon)
    canvasPasswordIcon.create_image(0, 0, anchor=NW, image=canvasPasswordIcon.image)

    # ---------------------------

    # username icon label
    usernameIcon = Image.open("assets/images/UI_Icons/Username_Icon.png")
    usernameIcon = usernameIcon.resize((48, 44))

    canvasUsernameIcon = Canvas(
        _registerWindow_, height=40, width=46, highlightthickness=0
    )

    canvasUsernameIcon.place(x=130, y=390)

    canvasUsernameIcon.image = ImageTk.PhotoImage(usernameIcon)

    canvasUsernameIcon.create_image(0, 0, anchor=NW, image=canvasUsernameIcon.image)

    # ---------------------------

    emailLabel = Label(
        _registerWindow_,
        text="email",
        font=quickSandBold(14),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )
    emailLabel.place(x=175, y=190, anchor="w")

    # ---------------------------
    passwordLabel = Label(
        _registerWindow_,
        text="password",
        font=quickSandBold(14),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )
    passwordLabel.place(x=175, y=302, anchor="w")

    # ---------------------------

    usernameLabel = Label(
        _registerWindow_,
        text="username",
        font=quickSandBold(14),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )
    usernameLabel.place(x=175, y=412, anchor="w")

    # ---------------------------

    inputEmail = Entry(
        _registerWindow_,
        width=30,
        borderwidth=0,
        font=quickSandBold(12),
        bg=colors["secondary-300"],
        fg=colors["secondary-500"],
        highlightthickness=0,
        cursor="xterm",
    )

    inputEmail.place(x=140, y=220)
    inputEmail.bind("<FocusIn>", lambda e: on_focus_in(e, inputEmail))
    inputEmail.bind("<FocusOut>", lambda e: on_focus_out(e, inputEmail))
    # ---------------------------

    inputPassword = Entry(
        _registerWindow_,
        width=30,
        borderwidth=0,
        font=quickSandBold(12),
        bg=colors["secondary-300"],
        fg=colors["secondary-500"],
        highlightthickness=0,
        show="*",
        cursor="xterm",
    )
    inputPassword.place(x=140, y=330)
    inputPassword.bind("<FocusIn>", lambda e: on_focus_in(e, inputPassword))
    inputPassword.bind("<FocusOut>", lambda e: on_focus_out(e, inputPassword))

    # ---------------------------

    inputUsername = Entry(
        _registerWindow_,
        width=30,
        borderwidth=0,
        font=quickSandBold(12),
        bg=colors["secondary-300"],
        fg=colors["secondary-500"],
        highlightthickness=0,
        cursor="xterm",
    )

    inputUsername.place(x=140, y=440)
    inputUsername.bind("<FocusIn>", lambda e: on_focus_in(e, inputUsername))
    inputUsername.bind("<FocusOut>", lambda e: on_focus_out(e, inputUsername))

    # ---------------------------

    #  manage password
    canvasManagePassword = Canvas(
        _registerWindow_, height=36, width=50, highlightthickness=0, cursor="hand2"
    )

    canvasManagePassword.config(highlightthickness=0, bd=0, bg=colors["primary-50"])

    # bind - when the user releases the key (onKeyPress), the function will be called
    inputPassword.bind(
        "<KeyRelease>",
        lambda event: manageVisibility(
            ImageTk, Image, canvasManagePassword, NW, inputPassword, 445, 325
        ),
    )

    # bind - when the user clicks (onClick) on the canvas, the function will be called
    canvasManagePassword.bind(
        "<Button-1>",
        lambda event: togglePasswordVisibility(
            ImageTk, Image, canvasManagePassword, NW, inputPassword, 445, 325
        ),
    )

    # ---------------------------

    labelInfo = tk.Label(
        _registerWindow_,
        text="Already have an account? Sign In!",
        font=quickSandRegular(12),
        bd=0,
        bg=colors["primary-50"],
        highlightthickness=0,
        fg=colors["secondary-500"],
        cursor="hand2",
    )

    labelInfo.place(x=164, y=500)
    labelInfo.bind("<Enter>", lambda e: label_on_enter(e, labelInfo))
    labelInfo.bind("<Leave>", lambda e: label_on_leave(e, labelInfo))
    labelInfo.bind(
        "<Button-1>",
        lambda event: openSignInLink(event, _registerWindow_, Window),
    )

    btnSignUp = Button(
        _registerWindow_,
        width=24,
        height=2,
        text="Sign Up",
        borderwidth=10,
        font=quickSandBold(13),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        activebackground=colors["accent-100"],
        cursor="hand2",
    )

    btnSignUp.place(x=164, y=570)
    # Hoover effect on the button
    btnSignUp.bind("<Enter>", lambda e: button_on_enter(e, btnSignUp))
    btnSignUp.bind("<Leave>", lambda e: button_on_leave(e, btnSignUp))

    _registerWindow_.bind(
        "<Button-1>",
        lambda e: on_click_outside(
            e, _registerWindow_, inputEmail, inputPassword, inputUsername
        ),
    )

    # bind - when the user clicks (onClick) on the button, will trigger checkRegister function
    btnSignUp.bind(
        "<Button-1>",
        lambda event: checkRegister(
            inputEmail.get(),
            inputPassword.get(),
            inputUsername.get(),
            _registerWindow_,
            Window,
        ),
    )

    _registerWindow_.grab_set()


def checkRegister(
    email: str, password: str, username: str, registerWindow: object, Window: object
) -> None:
    global isLogged, isNewUser

    """
    This function is used to check if the user can register or not.
    
    :param email: str
    :param password: str
    :param username: str
    :param registerWindow: object
    :param Window: object

    :return: None
    """

    if username == "" or email == "" or password == "":
        return messagebox.showerror(
            "Error", "All fields are required", parent=registerWindow
        )

    # checking if the username is valid
    elif checkUsername(username) == False:
        return messagebox.showerror("Error", "Invalid username", parent=registerWindow)

    # checking if the username already exists
    elif checkSignUpUsername(username) == False:
        return messagebox.showerror(
            "Error", "Username already exists", parent=registerWindow
        )

    # checking if the email is valid
    elif checkEmail(email) == False:
        return messagebox.showerror("Error", "Invalid email", parent=registerWindow)

    # check if the email already exists
    elif checkSignUpEmail(email) == False:
        return messagebox.showerror(
            "Error", "Email already exists", parent=registerWindow
        )

    else:
        # add the user to the database
        newUser = register(username, email, password)
       

        if newUser == True:
            messagebox.showinfo(
                "Success",
                f"We're glad you join our community {username}",
                parent=registerWindow,
            )

            isLogged = False
            isNewUser = True

            registerWindow.destroy()
            Window.destroy()

            homeWindow(email, isLogged, isNewUser)


def openSignInLink(event: object, registerWindow: object, window: object) -> None:
    from windows.Authentication.loginWindow import (
        loginWindow,
    )  # to fix the circular import issue

    """
    This function is used to open the sign in window.

    :param event: object
    :param registerWindow: object
    :param window: object

    :return: None
    """
    registerWindow.destroy()
    loginWindow(window)
