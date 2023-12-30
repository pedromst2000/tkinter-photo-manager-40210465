from tkinter import Tk
from styles.colors import colors
from models.users import getUserInfo


def homeWindow(email: str, isLogged: bool, isNewUser: bool) -> None:
    """
    This function is used to create the home window.

    :param email: str
    :param isLogged: bool
    :param isNewUser: bool

    :return: None

    """

    # open the window
    _homeWindow_ = Tk()

    # set the title
    _homeWindow_.title("PhotoShow - Home")
    _homeWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _homeWindow_.resizable(0, 0)
    _homeWindow_.geometry("1350x700")
    _homeWindow_.config(bg=colors["primary-50"])

    # # get the logged user payload
    loggedUser = getUserInfo(email)
    registerPayload = getUserInfo(email)  # get the user registered payload

    _homeWindow_.mainloop()
