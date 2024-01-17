import tkinter as tk
from styles.colors import colors

# Todo - Change the size of the window


def manageWindow():
    """
    This function is used to display the manage window.
    """

    # open the window
    _manageWindow_ = tk.Toplevel()

    # centering the window
    manageWindowWidth = 573  # width of the window
    manageWindowHeight = 580  # height of the window

    screenWidth = _manageWindow_.winfo_screenwidth()  # width of the screen

    screenHeight = _manageWindow_.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (manageWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (manageWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    _manageWindow_.geometry(
        "%dx%d+%d+%d" % (manageWindowWidth, manageWindowHeight, x, y)
    )
    _manageWindow_.title("🛠️ Manage 🛠️")
    _manageWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _manageWindow_.resizable(0, 0)
    _manageWindow_.config(bg=colors["primary-50"])

    _manageWindow_.grab_set()
