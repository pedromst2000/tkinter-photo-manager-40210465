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
)
from PIL import ImageTk, Image
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from models.users import getUserInfo, findUserID
from models.favorites import get_favorites_albuns
from models.photos import get_album_photos
from utils.profile.profile import (
    insert_favorite_albuns,
    selectFavoriteAlbum,
    previewSelectedPhoto,
)
from utils.widgets.button import (
    on_enter as button_on_enter,
    on_leave as button_on_leave,
)

# global variables
arrowRightIcon = ""
placeholderImage = ""
currentSelectedImage = ""
selectedAlbum = ""
current_index = 0


def favoritesProfileWindow(email: str):
    """
    This function is used to display favorites profile window.

    :param email: str
    """
    global arrowRightIcon, placeholderImage, currentSelectedImage, selectedAlbum, current_index

    # open the window
    _favoritesProfileWindow_ = Toplevel()

    userID = findUserID(email)  # replace with email
    userPayload = getUserInfo(userID)

    print(f"favoritesProfileWindowPayload: {userPayload}")

    # centering the window
    favoritesProfileWindowWidth = 1070  # width of the window
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

    # ---------------------------- Labels ---------------------------------

    yourFavoriteLabel = Label(
        _favoritesProfileWindow_,
        text="Your favorite albums",
        font=quickSandBold(20),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    yourFavoriteLabel.place(x=50, y=10)

    selectFavoriteLabel = Label(
        _favoritesProfileWindow_,
        text="Select a favorite album to see the available photos",
        font=quickSandRegular(12),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    selectFavoriteLabel.place(x=50, y=50)

    previewPhotosLabel = Label(
        _favoritesProfileWindow_,
        text="Preview photos",
        font=quickSandBold(16),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    previewPhotosLabel.place(x=790, y=70)

    # ---------------------------- Buttons ----------------------------------------------

    arrowRightIcon = ImageTk.PhotoImage(
        Image.open("assets/images/UI_Icons/arrow_right.png").resize((35, 35))
    )

    btnSelectFavoriteAlbum = Button(
        width=78,
        height=50,
        master=_favoritesProfileWindow_,
        image=arrowRightIcon,
        borderwidth=10,
        font=quickSandBold(16),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        command=CENTER,
        cursor="hand2",
    )

    btnSelectFavoriteAlbum.place(x=320, y=210)

    btnPrevImage = Button(
        width=4,
        height=1,
        master=_favoritesProfileWindow_,
        text="<",
        font=quickSandBold(20),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        command=CENTER,
        cursor="hand2",
    )

    btnPrevImage.place(x=720, y=380)

    btnNextImage = Button(
        width=4,
        height=1,
        master=_favoritesProfileWindow_,
        text=">",
        font=quickSandBold(20),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        command=CENTER,
        cursor="hand2",
    )

    btnNextImage.place(x=950, y=380)

    # ---------------------------- Favorites List Albuns ---------------------------------

    favoritesAlbunsListbox = Listbox(
        _favoritesProfileWindow_,
        width=22,
        height=10,
        font=quickSandRegular(12),
        bg=colors["secondary-500"],
        fg=colors["primary-50"],
        highlightthickness=0,
        borderwidth=0,
    )

    # change the selected background color
    favoritesAlbunsListbox["selectbackground"] = colors["secondary-300"]

    favoritesAlbunsListbox.place(x=50, y=120)

    favoritesAlbunsScrollbar = Scrollbar(
        _favoritesProfileWindow_,
        orient="vertical",
        command=favoritesAlbunsListbox.yview,
    )

    favoritesAlbunsScrollbar.place(x=270, y=120, height=250)

    favoritesAlbunsListbox.configure(yscrollcommand=favoritesAlbunsScrollbar.set)

    insert_favorite_albuns(get_favorites_albuns(userID), favoritesAlbunsListbox)
    # -------------------------------------- Photos List ------------------------------------------

    photosListbox = Listbox(
        _favoritesProfileWindow_,
        width=22,
        height=10,
        font=quickSandRegular(12),
        bg=colors["secondary-500"],
        fg=colors["primary-50"],
        highlightthickness=0,
        borderwidth=0,
    )

    # change the selected background color
    photosListbox["selectbackground"] = colors["secondary-300"]

    photosVScrollbar = Scrollbar(
        _favoritesProfileWindow_,
        orient="vertical",
        command=photosListbox.yview,
    )

    photosHScrollbar = Scrollbar(
        _favoritesProfileWindow_,
        orient="horizontal",
        command=photosListbox.xview,
    )

    photosVScrollbar.place(x=650, y=120, height=250)
    photosHScrollbar.place(x=430, y=370, width=220)

    photosListbox.config(yscrollcommand=photosVScrollbar.set)
    photosListbox.config(xscrollcommand=photosHScrollbar.set)

    photosListbox.place(x=430, y=120)

    # -------------------------------------- Preview Photos --------------------------------------

    placeholderImage = ImageTk.PhotoImage(
        Image.open("assets/images/photos_gallery/placeholder_image.png").resize(
            (295, 245)
        )
    )

    containerCanvas = Frame(
        _favoritesProfileWindow_,
        width=300,
        height=250,
        relief="sunken",
        border=3,
        bg=colors["secondary-300"],
    )

    containerCanvas.place(x=720, y=120)

    canvasPreviewImage = Canvas(
        _favoritesProfileWindow_,
        width=295,
        height=245,
        highlightthickness=0,
        borderwidth=0,
    )

    canvasPreviewImage.place(x=722, y=122)

    canvasPreviewImage.create_image(0, 0, image=placeholderImage, anchor=NW)

    # ----------------------------------Navigation Images--------------------------------------
    def showImage(index):
        """
        Helper function to display the image at the given index.
        """
        if 0 <= index < photosListbox.size():
            photoName = photosListbox.get(index)
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
        if len(photosListbox.curselection()) > 0:
            current_index = (current_index + 1) % photosListbox.size()
            if current_index < photosListbox.size():
                photosListbox.selection_clear(0, END)
                photosListbox.selection_set(current_index)
                showImage(current_index)
        else:
            messagebox.showerror(
                "Error",
                "You need to select an image to view the next one.",
                parent=_favoritesProfileWindow_,
            )

    def prevImage(event):
        """
        This function is used to preview the previous image.
        """
        global current_index
        if len(photosListbox.curselection()) > 0:
            current_index = (current_index - 1) % photosListbox.size()
            if current_index >= 0:
                photosListbox.selection_clear(0, END)
                photosListbox.selection_set(current_index)
                showImage(current_index)
        else:
            messagebox.showerror(
                "Error",
                "You need to select an image to view the previous one.",
                parent=_favoritesProfileWindow_,
            )

    # ---------------------------- Events -------------------------------------------------------
    btnSelectFavoriteAlbum.bind(
        "<Enter>",
        lambda e: button_on_enter(e, btnSelectFavoriteAlbum),
    )

    btnSelectFavoriteAlbum.bind(
        "<Leave>",
        lambda e: button_on_leave(e, btnSelectFavoriteAlbum),
    )

    btnPrevImage.bind(
        "<Enter>",
        lambda e: button_on_enter(e, btnPrevImage),
    )

    btnPrevImage.bind(
        "<Leave>",
        lambda e: button_on_leave(e, btnPrevImage),
    )

    btnNextImage.bind(
        "<Enter>",
        lambda e: button_on_enter(e, btnNextImage),
    )

    btnNextImage.bind(
        "<Leave>",
        lambda e: button_on_leave(e, btnNextImage),
    )

    btnSelectFavoriteAlbum.bind(
        "<Button-1>",
        lambda e: selectFavoriteAlbum(
            e,
            favoritesAlbunsListbox,
            photosListbox,
            userID,
            get_favorites_albuns,
            get_album_photos,
            messagebox,
            _favoritesProfileWindow_,
            selectedAlbum,
            current_index,
        ),
    )

    photosListbox.bind(
        "<<ListboxSelect>>",
        lambda event: previewSelectedPhoto(
            event, photosListbox, canvasPreviewImage, placeholderImage
        ),
    )

    btnPrevImage.bind("<Button-1>", lambda event: prevImage(event))
    btnNextImage.bind("<Button-1>", lambda event: nextImage(event))

    _favoritesProfileWindow_.grab_set()
