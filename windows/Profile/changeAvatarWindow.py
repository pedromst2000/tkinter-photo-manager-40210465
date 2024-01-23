from tkinter import Canvas, NW, messagebox, Toplevel, Label, Button, filedialog
from PIL import ImageTk, Image
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from models.users import getUserInfo, findUserID, saveAvatar
from utils.widgets.button import (
    on_enter as button_on_enter,
    on_leave as button_on_leave,
)

image = ""
photo_image = ""
statusBtn = "disabled"
cursorBtn = "arrow"


def uploadAvatar(
    event: callable, canvasAvatar: Canvas, btnSaveAvatar: Button, userID: int
):
    """
    This function is used to upload the avatar.

    :param event: callable
    :param canvasAvatar: Canvas
    :param btnSaveAvatar: Button
    """

    global image, photo_image, statusBtn, cursorBtn

    # open the file dialog
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select an image",
        filetypes=(
            ("png files", "*.png"),
            ("jpg files", "*.jpg"),
            ("jpeg files", "*.jpeg"),
        ),
    )

    if filename == "":
        return

    if filename != "":
        image_path = filename

        image = Image.open(image_path)

        image = image.resize((200, 200))

        photo_image = ImageTk.PhotoImage(image)  # Store as an instance variable

        canvasAvatar.create_image(0, 0, anchor=NW, image=photo_image)

        image = image_path  # assigning the global variable image to the image_path

        canvasAvatar.image = photo_image

        statusBtn = "normal"
        cursorBtn = "hand2"

        btnSaveAvatar["state"] = statusBtn
        btnSaveAvatar["cursor"] = cursorBtn
        btnSaveAvatar.bind("<Enter>", lambda e: button_on_enter(e, btnSaveAvatar))
        btnSaveAvatar.bind("<Leave>", lambda e: button_on_leave(e, btnSaveAvatar))
        btnSaveAvatar.bind(
            "<Button-1>", lambda event: _saveAvatar_(event, image_path, userID)
        )


def _saveAvatar_(event: callable, avatar: str, userID: int):
    """
    This function is used to save the avatar.

    :param event: callable
    :param avatar: str
    :param userID: int

    """

    # slicing the path to get only the image name
    avatar = avatar.split("/")[-1]

    saveAvatar(userID, avatar)

    messagebox.showinfo("Success", "Avatar changed successfully!")


def changeAvatarWindow(email: str):
    """
    This function is used to display change avatar window.

    :param email: str
    """

    global avatarImage

    # open the window
    _changeAvatarWindow_ = Toplevel()

    userID = findUserID(email)
    userPayload = getUserInfo(userID)
    lambda event: _saveAvatar_(event, avatarImage, userID)

    # centering the window
    changeAvatarWindowWidth = 500  # width of the window
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

    # ----------------------  Labels -----------------------------------

    changeAvatarLabel = Label(
        _changeAvatarWindow_,
        text="Change Avatar",
        font=quickSandBold(22),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    changeAvatarLabel.place(x=140, y=15)

    helpLabel = Label(
        _changeAvatarWindow_,
        text="Select a new avatar for your profile",
        font=quickSandRegular(12),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    helpLabel.place(x=125, y=70)

    # ----------------------  Buttons -----------------------------------

    btnChangeAvatar = Button(
        _changeAvatarWindow_,
        width=16,
        height=2,
        text="Upload Avatar",
        borderwidth=10,
        font=quickSandBold(12),
        fg=colors["secondary-500"],
        background=colors["accent-300"],
        highlightthickness=0,
        activebackground=colors["accent-100"],
        cursor="hand2",
        compound="center",
        border=0,
    )

    btnChangeAvatar.place(x=170, y=380)

    btnSaveAvatar = Button(
        _changeAvatarWindow_,
        width=16,
        height=2,
        state=statusBtn,
        text="Save Avatar",
        borderwidth=10,
        font=quickSandBold(12),
        fg=colors["secondary-500"],
        background=colors["accent-300"],
        highlightthickness=0,
        activebackground=colors["accent-100"],
        cursor=cursorBtn,
        compound="center",
        border=0,
    )

    btnSaveAvatar.place(x=170, y=470)

    # ----------------------  Preeview Avatar -----------------------------------

    canvasPreeviewAvatar = Canvas(
        _changeAvatarWindow_,
        width=200,
        height=200,
        bg=colors["primary-50"],
        highlightthickness=0,
    )

    canvasPreeviewAvatar.place(x=150, y=135)

    avatarImage = Image.open(userPayload["avatar"])

    avatarImage = avatarImage.resize((200, 200))

    avatarImage = ImageTk.PhotoImage(avatarImage)

    canvasPreeviewAvatar.create_image(0, 0, image=avatarImage, anchor=NW)

    # ----------------------  Events -----------------------------------
    btnChangeAvatar.bind("<Enter>", lambda e: button_on_enter(e, btnChangeAvatar))
    btnChangeAvatar.bind("<Leave>", lambda e: button_on_leave(e, btnChangeAvatar))
    btnChangeAvatar.bind(
        "<Button-1>",
        lambda event: uploadAvatar(event, canvasPreeviewAvatar, btnSaveAvatar, userID),
    )

    _changeAvatarWindow_.grab_set()
