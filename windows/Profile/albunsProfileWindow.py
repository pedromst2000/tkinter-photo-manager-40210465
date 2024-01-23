from tkinter import (
    Canvas,
    NW,
    CENTER,
    messagebox,
    Toplevel,
    END,
    Frame,
    Label,
    Listbox,
    Scrollbar,
    Button,
    Entry,
)
from PIL import ImageTk, Image
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from models.users import getUserInfo, findUserID
from models.albuns import get_user_albuns, edit_album, get_albuns, add_album
from models.photos import get_album_photos, remove_photo, get_all_photos
from utils.widgets.button import (
    on_enter as button_on_enter,
    on_leave as button_on_leave,
)
from utils.widgets.input import on_click_outside, on_focus_in, on_focus_out
from utils.profile.profile import (
    insert_albuns,
    selectAlbum,
    previewSelectedPhoto,
    editAlbumName,
    addAlbum,
    removePhoto,
)


# global variables
arrowRightIcon = ""
placeholderImage = ""
currentSelectedImage = ""
selectedAlbum = ""
editIcon = ""
addIcon = ""
current_index = 0


def albunsProfileWindow(email: str):
    """
    This function is used to display albuns profile window.

    :param email: str
    """

    global arrowRightIcon, placeholderImage, currentSelectedImage, editIcon, addIcon, selectedAlbum, current_index

    # open the window
    _albunsProfileWindow_ = Toplevel()

    userID = findUserID(email)  # replace with email
    userPayload = getUserInfo(userID)

    print(f"albunsProfileWindowPayload: {userPayload}")

    # centering the window
    albunsProfileWindowWidth = 1100  # width of the window
    albunsProfileWindowHeight = 595  # height of the window

    screenWidth = _albunsProfileWindow_.winfo_screenwidth()  # width of the screen

    screenHeight = _albunsProfileWindow_.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (albunsProfileWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (albunsProfileWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    _albunsProfileWindow_.geometry(
        "%dx%d+%d+%d" % (albunsProfileWindowWidth, albunsProfileWindowHeight, x, y)
    )
    _albunsProfileWindow_.title("👤 Profile - Albuns 📷🖼️")
    _albunsProfileWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _albunsProfileWindow_.resizable(0, 0)
    _albunsProfileWindow_.config(bg=colors["primary-50"])
    # ---------------------------------Labels---------------------------------

    selectLabel = Label(
        _albunsProfileWindow_,
        text="Select an album to view the available photos",
        font=quickSandBold(12),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    selectLabel.place(x=20, y=20)

    previewLabel = Label(
        _albunsProfileWindow_,
        text="Preview Photos",
        font=quickSandBold(16),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    previewLabel.place(x=790, y=20)

    editAlbumNameLabel = Label(
        _albunsProfileWindow_,
        text="Edit Album Name",
        font=quickSandBold(13),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    editAlbumNameLabel.place(x=20, y=326)

    addAlbumLabel = Label(
        _albunsProfileWindow_,
        text="Add Album",
        font=quickSandBold(13),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    addAlbumLabel.place(x=20, y=446)

    # --------------------------------Albuns List--------------------------------
    albunsListbox = Listbox(
        _albunsProfileWindow_,
        width=22,
        height=10,
        font=quickSandRegular(12),
        bg=colors["secondary-500"],
        fg=colors["primary-50"],
        highlightthickness=0,
        borderwidth=0,
    )

    # change the selected background color
    albunsListbox["selectbackground"] = colors["secondary-300"]

    albunsListbox.place(x=25, y=60)

    albunsScrollbar = Scrollbar(
        _albunsProfileWindow_,
        orient="vertical",
        command=albunsListbox.yview,
    )

    albunsScrollbar.place(x=240, y=60, height=250)

    insert_albuns(get_user_albuns(userID), albunsListbox)

    albunsListbox.config(yscrollcommand=albunsScrollbar.set)

    arrowRightIcon = ImageTk.PhotoImage(
        Image.open("assets/images/UI_Icons/arrow_right.png").resize((35, 35))
    )
    # ---------------------------------Buttons--------------------------------------

    # TODO: will not show the add album button for a visitor user (Nice to have)
    # TODO: will not show the edit album button for a visitor user (Nice to have)
    # TODO: will not show the remove photo button for a visitor user (Nice to have)
    # TODO: Willl not show the labels of the inputs for a visitor user (Nice to have)
    # TODO: Will not show the inputs for a visitor user (Nice to have)
    # TODO: The favorite button will only show for a visitor user (Nice to have)

    btnSelectAlbum = Button(
        width=78,
        height=50,
        master=_albunsProfileWindow_,
        image=arrowRightIcon,
        borderwidth=10,
        font=quickSandBold(16),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        command=CENTER,
        cursor="hand2",
    )

    btnSelectAlbum.place(x=280, y=200)

    btnPrevImage = Button(
        width=4,
        height=1,
        master=_albunsProfileWindow_,
        text="<",
        font=quickSandBold(20),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        command=CENTER,
        cursor="hand2",
    )

    btnPrevImage.place(x=720, y=350)

    btnNextImage = Button(
        width=4,
        height=1,
        master=_albunsProfileWindow_,
        text=">",
        font=quickSandBold(20),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        command=CENTER,
        cursor="hand2",
    )

    btnNextImage.place(x=950, y=350)

    editIcon = ImageTk.PhotoImage(
        Image.open("assets/images/UI_Icons/Edit_ICON.png").resize((25, 25))
    )

    btnEditAlbum = Button(
        width=200,
        height=40,
        master=_albunsProfileWindow_,
        borderwidth=10,
        font=quickSandBold(15),
        background=colors["accent-300"],
        highlightthickness=0,
        activebackground=colors["accent-100"],
        cursor="hand2",
        compound="center",
        border=0,
        image=editIcon,
    )

    # place under the input
    btnEditAlbum.place(x=25, y=400)

    addIcon = ImageTk.PhotoImage(
        Image.open("assets/images/UI_Icons/Add_Icon.png").resize((35, 35))
    )

    btnAddAlbum = Button(
        width=200,
        height=40,
        master=_albunsProfileWindow_,
        borderwidth=10,
        font=quickSandBold(15),
        background=colors["accent-300"],
        highlightthickness=0,
        activebackground=colors["accent-100"],
        cursor="hand2",
        compound="center",
        border=0,
        image=addIcon,
    )

    btnAddAlbum.place(x=25, y=520)

    btnDeletePhoto = Button(
        width=16,
        height=1,
        master=_albunsProfileWindow_,
        text="Delete Photo",
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

    btnDeletePhoto.place(x=400, y=480)

    btnAddFavorite = Button(
        width=22,
        height=2,
        master=_albunsProfileWindow_,
        text="Add to Favorite albums",
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

    # btnAddFavorite.place(x=25, y=340)

    # --------------------------------Photos List-----------------------------------

    placeholderImage = ImageTk.PhotoImage(
        Image.open("assets/images/photos_gallery/placeholder_image.png").resize(
            (295, 245)
        )
    )

    listAlbumPhotos = Listbox(
        _albunsProfileWindow_,
        width=22,
        height=15,
        font=quickSandRegular(12),
        bg=colors["secondary-500"],
        fg=colors["primary-50"],
        highlightthickness=0,
        borderwidth=0,
    )

    listAlbumPhotos["selectbackground"] = colors["secondary-300"]
    listAlbumPhotos.place(x=380, y=60)

    photosVScrollbar = Scrollbar(
        _albunsProfileWindow_,
        orient="vertical",
        command=listAlbumPhotos.yview,
    )

    photosHScrollbar = Scrollbar(
        _albunsProfileWindow_,
        orient="horizontal",
        command=listAlbumPhotos.xview,
    )

    photosVScrollbar.place(x=595, y=60, height=375)
    photosHScrollbar.place(x=380, y=435, width=215)

    listAlbumPhotos.config(yscrollcommand=photosVScrollbar.set)
    listAlbumPhotos.config(xscrollcommand=photosHScrollbar.set)

    # ---------------------------------NAVIGATION IMAGES---------------------------------

    containerCanvas = Frame(
        _albunsProfileWindow_,
        width=300,
        height=250,
        relief="sunken",
        border=3,
        bg=colors["secondary-300"],
    )

    containerCanvas.place(x=720, y=80)

    canvasPreviewImage = Canvas(
        _albunsProfileWindow_,
        width=295,
        height=245,
        highlightthickness=0,
        borderwidth=0,
    )

    canvasPreviewImage.place(x=722, y=82)

    canvasPreviewImage.create_image(0, 0, image=placeholderImage, anchor=NW)

    def showImage(index):
        """
        Helper function to display the image at the given index.
        """
        if 0 <= index < listAlbumPhotos.size():
            photoName = listAlbumPhotos.get(index)
            currentSelectedImage = ImageTk.PhotoImage(
                Image.open(f"{photoName}").resize((295, 245))
            )
            canvasPreviewImage.create_image(0, 0, image=currentSelectedImage, anchor=NW)
            canvasPreviewImage.image = currentSelectedImage

    def nextImage(event):
        """
        This function is used to preview the next image.
        """
        global current_index
        if len(listAlbumPhotos.curselection()) > 0:
            current_index = (current_index + 1) % listAlbumPhotos.size()
            if current_index < listAlbumPhotos.size():
                listAlbumPhotos.selection_clear(0, END)
                listAlbumPhotos.selection_set(current_index)
                showImage(current_index)
        else:
            messagebox.showerror(
                "Error",
                "You need to select an image to view the next one.",
                parent=_albunsProfileWindow_,
            )

    def prevImage(event):
        """
        This function is used to preview the previous image.
        """
        global current_index
        if len(listAlbumPhotos.curselection()) > 0:
            current_index = (current_index - 1) % listAlbumPhotos.size()
            if current_index >= 0:
                listAlbumPhotos.selection_clear(0, END)
                listAlbumPhotos.selection_set(current_index)
                showImage(current_index)
        else:
            messagebox.showerror(
                "Error",
                "You need to select an image to view the previous one.",
                parent=_albunsProfileWindow_,
            )

    # ---------------------------------INPUTS--------------------------------
    editAlbumInput = Entry(
        _albunsProfileWindow_,
        width=20,
        font=quickSandBold(12),
        bg=colors["secondary-300"],
        fg=colors["primary-50"],
        highlightthickness=0,
        borderwidth=0,
    )

    editAlbumInput.place(x=25, y=360)

    addAlbumInput = Entry(
        _albunsProfileWindow_,
        width=20,
        font=quickSandBold(12),
        bg=colors["secondary-300"],
        fg=colors["primary-50"],
        highlightthickness=0,
        borderwidth=0,
        cursor="xterm",
    )

    addAlbumInput.place(x=25, y=480)

    # ---------------------------------Events---------------------------------
    listAlbumPhotos.bind(
        "<<ListboxSelect>>",
        lambda event: previewSelectedPhoto(
            event, listAlbumPhotos, canvasPreviewImage, placeholderImage
        ),
    )
    btnSelectAlbum.bind(
        "<Button-1>",
        lambda event: selectAlbum(
            event,
            albunsListbox,
            userID,
            listAlbumPhotos,
            get_user_albuns,
            get_album_photos,
            messagebox,
            _albunsProfileWindow_,
        ),
    )
    btnSelectAlbum.bind("<Enter>", lambda e: button_on_enter(e, btnSelectAlbum))
    btnSelectAlbum.bind("<Leave>", lambda e: button_on_leave(e, btnSelectAlbum))
    btnPrevImage.bind("<Enter>", lambda e: button_on_enter(e, btnPrevImage))
    btnPrevImage.bind("<Leave>", lambda e: button_on_leave(e, btnPrevImage))
    btnNextImage.bind("<Enter>", lambda e: button_on_enter(e, btnNextImage))
    btnNextImage.bind("<Leave>", lambda e: button_on_leave(e, btnNextImage))
    btnAddAlbum.bind("<Enter>", lambda e: button_on_enter(e, btnAddAlbum))
    btnAddAlbum.bind("<Leave>", lambda e: button_on_leave(e, btnAddAlbum))
    btnAddAlbum.bind(
        "<Button-1>",
        lambda event: addAlbum(
            event,
            addAlbumInput,
            userID,
            get_user_albuns,
            add_album,
            messagebox,
            _albunsProfileWindow_,
            get_albuns,
            albunsListbox,
        ),
    )
    btnEditAlbum.bind("<Enter>", lambda e: button_on_enter(e, btnEditAlbum))
    btnEditAlbum.bind("<Leave>", lambda e: button_on_leave(e, btnEditAlbum))
    btnDeletePhoto.bind("<Enter>", lambda e: button_on_enter(e, btnDeletePhoto))
    btnDeletePhoto.bind("<Leave>", lambda e: button_on_leave(e, btnDeletePhoto))
    btnDeletePhoto.bind(
        "<Button-1>",
        lambda event: removePhoto(
            event,
            listAlbumPhotos,
            canvasPreviewImage,
            placeholderImage,
            get_all_photos,
            remove_photo,
            messagebox,
            _albunsProfileWindow_,
        ),
    )
    btnPrevImage.bind("<Button-1>", lambda event: prevImage(event))
    btnNextImage.bind("<Button-1>", lambda event: nextImage(event))
    editAlbumInput.bind("<FocusIn>", lambda event: on_focus_in(event, editAlbumInput))
    editAlbumInput.bind("<FocusOut>", lambda event: on_focus_out(event, editAlbumInput))
    addAlbumInput.bind("<FocusIn>", lambda event: on_focus_in(event, addAlbumInput))
    addAlbumInput.bind("<FocusOut>", lambda event: on_focus_out(event, addAlbumInput))
    btnEditAlbum.bind(
        "<Button-1>",
        lambda event: editAlbumName(
            event,
            albunsListbox,
            editAlbumInput,
            userID,
            get_user_albuns,
            edit_album,
            messagebox,
            _albunsProfileWindow_,
            get_albuns,
        ),
    )
    btnAddFavorite.bind("<Enter>", lambda e: button_on_enter(e, btnAddFavorite))
    btnAddFavorite.bind("<Leave>", lambda e: button_on_leave(e, btnAddFavorite))
    _albunsProfileWindow_.bind(
        "<Button-1>",
        lambda e: on_click_outside(
            e, _albunsProfileWindow_, editAlbumInput, addAlbumInput
        ),
    )

    _albunsProfileWindow_.grab_set()
