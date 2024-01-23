from tkinter import Tk, Canvas, NW, messagebox, Toplevel, Label
from PIL import ImageTk, Image
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from models.users import getUserInfo, findUserID


def favoritesProfileWindow(email: str):
    """
    This function is used to display favorites profile window.

    :param email: str
    """
    # open the window
    _favoritesProfileWindow_ = Toplevel()

    userID = findUserID("pedromst@gmail.com")  # replace with email
    userPayload = getUserInfo(userID)

    print(f"favoritesProfileWindowPayload: {userPayload}")

    # centering the window
    favoritesProfileWindowWidth = 1000  # width of the window
    favoritesProfileWindowHeight = 595  # height of the window

    screenWidth = _favoritesProfileWindow_.winfo_screenwidth()  # width of the screen

    screenHeight = _favoritesProfileWindow_.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (favoritesProfileWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (favoritesProfileWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    _favoritesProfileWindow_.geometry(
        "%dx%d+%d+%d"
        % (favoritesProfileWindowWidth, favoritesProfileWindowHeight, x, y)
    )
    _favoritesProfileWindow_.title("👤 Profile - Favorites ✨")
    _favoritesProfileWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _favoritesProfileWindow_.resizable(0, 0)
    _favoritesProfileWindow_.config(bg=colors["primary-50"])

    _favoritesProfileWindow_.grab_set()
