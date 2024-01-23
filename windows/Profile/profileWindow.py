from tkinter import Canvas, NW, Label, Button, Toplevel
from PIL import ImageTk, Image
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from windows.Profile.albunsProfileWindow import albunsProfileWindow
from windows.Profile.changePasswordWindow import changePasswordWindow
from windows.Profile.contactsWindow import contactsWindow
from windows.Profile.favoritesProfileWindow import favoritesProfileWindow
from windows.Profile.changeAvatarWindow import changeAvatarWindow
from models.users import getUserInfo, findUserID
from utils.widgets.button import (
    on_enter as button_on_enter,
    on_leave as button_on_leave,
)


# # fallback images
backgroundProfile = ""
followersImageIcon = ""
avatarImage = ""


def profileWindow(email: str):
    """
    This function is used to display the profile window.

    :param email: str
    """

    global backgroundProfile, followersImageIcon, avatarImage

    # open the window
    _profileWindow_ = Toplevel()

    userID = findUserID(email)  # replace with email
    userPayload = getUserInfo(userID)
    
    print(userPayload)

    # centering the window
    profileWindowWidth = 1000  # width of the window
    profileWindowHeight = 450  # height of the window

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

    backgroundProfile = Image.open("assets/images/profile/backgroundProfile.png")
    backgroundProfile = backgroundProfile.resize((profileWindowWidth, 220))

    avatarImage = Image.open(userPayload["avatar"])
    avatarImage = avatarImage.resize((130, 130))

    followersImageIcon = Image.open("assets/images/UI_Icons/followersIcon.png")
    followersImageIcon = followersImageIcon.resize((20, 20))

    canvasBackgroundProfile = Canvas(
        _profileWindow_,
        width=profileWindowWidth,
        height=220,
        highlightthickness=0,
        borderwidth=0,
    )

    canvasBackgroundProfile.place(x=0, y=0)

    canvasBackgroundProfile.image = ImageTk.PhotoImage(backgroundProfile)

    canvasBackgroundProfile.create_image(
        0, 0, image=canvasBackgroundProfile.image, anchor=NW
    )

    avatarCanvas = Canvas(
        _profileWindow_,
        width=130,
        height=130,
        highlightthickness=0,
        borderwidth=0,
    )
    avatarCanvas.place(x=40, y=40)

    avatarCanvas.image = ImageTk.PhotoImage(avatarImage)
    avatarCanvas.create_image(0, 0, image=avatarCanvas.image, anchor=NW)

    canvasBackgroundProfile.create_text(
        200,
        50,
        text=f"{userPayload['username']}",
        font=quickSandBold(20),
        anchor=NW,
        fill=colors["primary-50"],
    )

    roleLabel = Label(
        _profileWindow_,
        text=f"{userPayload['role']}",
        font=quickSandBold(12)
        if userPayload["role"] == "admin"
        else quickSandRegular(12),
        bg=colors["primary-50"]
        if userPayload["role"] == "admin"
        else colors["secondary-400"],
        fg=colors["secondary-500"]
        if userPayload["role"] == "admin"
        else colors["primary-50"],
    )

    roleLabel.place(x=200, y=100)

    canvasBackgroundProfile.create_text(
        850,
        175,
        text=f"{userPayload['followers']} followers",
        font=quickSandRegular(12),
        anchor=NW,
        fill=colors["primary-50"],
    )

    followersImageIcon = ImageTk.PhotoImage(followersImageIcon)

    canvasBackgroundProfile.create_image(820, 177, image=followersImageIcon, anchor=NW)

    canvasBackgroundProfile.create_text(
        710,
        175,
        text=f"{userPayload['photos']} photos",
        font=quickSandBold(12),
        anchor=NW,
        fill=colors["primary-50"],
    )

    # ------------------------- Buttons ----------------------------------------------
    albunsBtn = Button(
        _profileWindow_,
        width=18,
        height=2,
        text="Albuns",
        borderwidth=10,
        font=quickSandBold(13),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        activebackground=colors["accent-100"],
        fg=colors["secondary-500"],
        cursor="hand2",
    )

    favoritesBtn = Button(
        _profileWindow_,
        width=18,
        height=2,
        text="Favorites",
        borderwidth=10,
        font=quickSandBold(13),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        activebackground=colors["accent-100"],
        fg=colors["secondary-500"],
        cursor="hand2",
    )

    changePasswordBtn = Button(
        _profileWindow_,
        width=18,
        height=2,
        text="Change Password",
        borderwidth=10,
        font=quickSandBold(13),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        activebackground=colors["accent-100"],
        fg=colors["secondary-500"],
        cursor="hand2",
    )

    changeAvatarBtn = Button(
        _profileWindow_,
        width=18,
        height=2,
        text="Change Avatar",
        borderwidth=10,
        font=quickSandBold(13),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        activebackground=colors["accent-100"],
        fg=colors["secondary-500"],
        cursor="hand2",
    )

    contactsBtn = Button(
        _profileWindow_,
        width=18,
        height=2,
        text="Contacts",
        borderwidth=10,
        font=quickSandBold(13),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        activebackground=colors["accent-100"],
        fg=colors["secondary-500"],
        cursor="hand2",
    )

    # TODO = If is a visitor, show only the albuns and favorites buttons

    albunsBtn.place(x=40, y=270) if userPayload["role"] == "admin" or userPayload[
        "role"
    ] == "regular" else None
    favoritesBtn.place(x=240, y=270) if userPayload["role"] == "admin" or userPayload[
        "role"
    ] == "regular" else None
    changePasswordBtn.place(x=440, y=270)
    changeAvatarBtn.place(x=640, y=270)
    contactsBtn.place(x=40, y=350) if userPayload["role"] == "admin" else None

    # ------------------------- Events ----------------------------------------------

    albunsBtn.bind("<Enter>", lambda e: button_on_enter(e, albunsBtn))
    albunsBtn.bind("<Leave>", lambda e: button_on_leave(e, albunsBtn))
    favoritesBtn.bind("<Enter>", lambda e: button_on_enter(e, favoritesBtn))
    favoritesBtn.bind("<Leave>", lambda e: button_on_leave(e, favoritesBtn))
    changePasswordBtn.bind("<Enter>", lambda e: button_on_enter(e, changePasswordBtn))
    changePasswordBtn.bind("<Leave>", lambda e: button_on_leave(e, changePasswordBtn))
    changeAvatarBtn.bind("<Enter>", lambda e: button_on_enter(e, changeAvatarBtn))
    changeAvatarBtn.bind("<Leave>", lambda e: button_on_leave(e, changeAvatarBtn))
    contactsBtn.bind("<Enter>", lambda e: button_on_enter(e, contactsBtn))
    contactsBtn.bind("<Leave>", lambda e: button_on_leave(e, contactsBtn))
    albunsBtn.bind("<Button-1>", lambda event: albunsProfileWindow(email))
    favoritesBtn.bind("<Button-1>", lambda event: favoritesProfileWindow(email))
    changePasswordBtn.bind("<Button-1>", lambda event: changePasswordWindow(email))
    contactsBtn.bind("<Button-1>", lambda event: contactsWindow(email))
    changeAvatarBtn.bind("<Button-1>", lambda event: changeAvatarWindow(email))

    _profileWindow_.grab_set()
