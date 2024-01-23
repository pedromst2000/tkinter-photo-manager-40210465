from tkinter import Tk, Canvas, NW, messagebox, Toplevel, Label
from PIL import ImageTk, Image
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from models.users import getUserInfo, findUserID


def changeAvatarWindow(email: str):
    """
    This function is used to display change avatar window.

    :param email: str
    """
    # open the window
    _changeAvatarWindow_ = Toplevel()

    userID = findUserID("pedromst@gmail.com")  # replace with email
    userPayload = getUserInfo(userID)

    print(f"albunsProfileWindowPayload: {userPayload}")

    # centering the window
    changeAvatarWindowWidth = 1000  # width of the window
    changeAvatarWindowHeight = 595  # height of the window

    screenWidth = _changeAvatarWindow_.winfo_screenwidth()  # width of the screen

    screenHeight = _changeAvatarWindow_.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (changeAvatarWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (changeAvatarWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    _changeAvatarWindow_.geometry(
        "%dx%d+%d+%d" % (changeAvatarWindowWidth, changeAvatarWindowHeight, x, y)
    )
    _changeAvatarWindow_.title("👤 Profile - Change Avatar 👤")
    _changeAvatarWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _changeAvatarWindow_.resizable(0, 0)
    _changeAvatarWindow_.config(bg=colors["primary-50"])

    _changeAvatarWindow_.grab_set()
