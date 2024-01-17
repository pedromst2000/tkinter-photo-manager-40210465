from tkinter import Tk, Canvas, NW, messagebox
from PIL import ImageTk, Image
from styles.colors import colors
from models.users import getUserInfo, findUserID
from classes.Menu import menu


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
    homeCanvas = Canvas(_homeWindow_, width=1350, height=700)
    homeCanvas.place(x=0, y=0)

    homeImage = Image.open("assets/images/main_background.png")
    homeImage = homeImage.resize((1350, 700))

    homeImage = ImageTk.PhotoImage(homeImage)

    homeCanvas.create_image(0, 0, image=homeImage, anchor=NW)

    backgroundMenu = Image.open("assets/images/home/menu/backgroundMenu.png")
    backgroundMenu = backgroundMenu.resize((1145, 396))

    backgroundMenu = ImageTk.PhotoImage(backgroundMenu)

    # centering the image on the canvas
    x = (1350 - 1145) / 2
    y = (700 - 396) / 2

    homeCanvas.create_image(x, y, image=backgroundMenu, anchor=NW)

    logoImage = Image.open("assets/images/Logo.png")
    logoImage = logoImage.resize((306, 65))

    logoImage = ImageTk.PhotoImage(logoImage)
    homeCanvas.create_image(522, 180, image=logoImage, anchor=NW)

    userID = findUserID(email)
    userPayload = getUserInfo(userID)

    _menu_ = menu(homeCanvas=homeCanvas, homeWindow=_homeWindow_)

    if isNewUser:
        messagebox.showinfo(
            "Welcome to PhotoShow!",
            "Where every pixel tells a tale, you can now enjoy your time with us.\n\n"
            "Let's take a look at our features:\n\n"
            "  - 🌐 Explore: Explore the world of photos with other users\n\n"
            "  - 👤 Profile: Edit your profile and view your photos and albums\n\n"
            "  - 🔔 Notifications: Stay updated with news through notifications\n\n"
            "  - 📈 Dashboard: Check your dashboard for statistics",
        )

    if (
        isLogged
        and userPayload["role"] == "regular"
        or userPayload["role"] == "unsigned"
    ):
        _menu_.regularMenu()

    if isLogged and userPayload["role"] == "admin":
        _menu_.adminMenu()

    _homeWindow_.mainloop()
