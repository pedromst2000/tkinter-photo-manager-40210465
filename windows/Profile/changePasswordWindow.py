from tkinter import Tk, Canvas, NW, messagebox, Toplevel, Label
from PIL import ImageTk, Image
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from models.users import getUserInfo, findUserID


def changePasswordWindow(email: str):
    """
    This function is used to display change password window.

    :param email: str
    """
    # open the window
    _changePasswordWindow_ = Toplevel()

    userID = findUserID("pedromst@gmail.com")  # replace with email
    userPayload = getUserInfo(userID)

    print(f"changePasswordWindowPayload: {userPayload}")

    # centering the window
    changePasswordWindowWidth = 1000  # width of the window
    changePasswordWindowHeight = 595  # height of the window

    screenWidth = _changePasswordWindow_.winfo_screenwidth()  # width of the screen

    screenHeight = _changePasswordWindow_.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (changePasswordWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (changePasswordWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    _changePasswordWindow_.geometry(
        "%dx%d+%d+%d" % (changePasswordWindowWidth, changePasswordWindowHeight, x, y)
    )
    _changePasswordWindow_.title("👤 Profile - Change Password 🔒🔑")
    _changePasswordWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _changePasswordWindow_.resizable(0, 0)
    _changePasswordWindow_.config(bg=colors["primary-50"])

    _changePasswordWindow_.grab_set()
