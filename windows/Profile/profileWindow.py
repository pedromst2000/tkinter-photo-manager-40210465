import tkinter as tk
from styles.colors import colors


# Todo - Change the size of the window


def profileWindow():
    """
    This function is used to display the profile window.
    """

    # open the window
    _profileWindow_ = tk.Toplevel()

    # centering the window
    profileWindowWidth = 573  # width of the window
    profileWindowHeight = 580  # height of the window

    screenWidth = _profileWindow_.winfo_screenwidth()  # width of the screen

    screenHeight = _profileWindow_.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (profileWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (profileWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    _profileWindow_.geometry(
        "%dx%d+%d+%d" % (profileWindowWidth, profileWindowHeight, x, y)
    )
    _profileWindow_.title("👤 Profile 👤")
    _profileWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _profileWindow_.resizable(0, 0)
    _profileWindow_.config(bg=colors["primary-50"])

    _profileWindow_.grab_set()
