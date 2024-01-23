from tkinter import Tk, Canvas, NW, messagebox, Toplevel, Label
from PIL import ImageTk, Image
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from models.users import getUserInfo, findUserID


def contactsWindow(email: str):
    """
    This function is used to display the admin contacts of banned users window.

    :param email: str
    """
    # open the window
    _contactsWindow_ = Toplevel()

    userID = findUserID("pedromst@gmail.com")  # replace with email
    userPayload = getUserInfo(userID)

    print(f"contactsWindowPayload: {userPayload}")

    # centering the window
    contactsWindowWidth = 1000  # width of the window
    contactsWindowHeight = 595  # height of the window

    screenWidth = _contactsWindow_.winfo_screenwidth()  # width of the screen

    screenHeight = _contactsWindow_.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (contactsWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (contactsWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    _contactsWindow_.geometry(
        "%dx%d+%d+%d" % (contactsWindowWidth, contactsWindowHeight, x, y)
    )
    _contactsWindow_.title("👤 Profile - Contacts 👥")
    _contactsWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _contactsWindow_.resizable(0, 0)
    _contactsWindow_.config(bg=colors["primary-50"])

    _contactsWindow_.grab_set()
