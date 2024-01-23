from tkinter import Listbox, messagebox, Toplevel, Canvas, NW, END, Entry
from PIL import ImageTk, Image


def insert_albuns(albuns: list, albunsListbox: Listbox):
    """
    This function is used to insert the albuns into the listbox.

    :param albuns: list
    :param albunsListbox: tk.Listbox

    """

    if len(albuns) == 0:
        albunsListbox.insert("end", "No albums available.")

    for album in albuns:
        albunsListbox.insert("end", album["name"])


def insert_favorite_albuns(favorite_albuns: list, favoriteAlbunsListbox: Listbox):
    """
    This function is used to insert the favorite albuns into the listbox.

    :param favorite_albuns: list
    :param favoriteAlbunsListbox: tk.Listbox

    """

    if len(favorite_albuns) == 0:
        favoriteAlbunsListbox.insert("end", "No favorite albums available.")

    for album in favorite_albuns:
        favoriteAlbunsListbox.insert("end", album["name"])


def insert_contacts(contacts: list, contactsListbox: Listbox):
    """
    This function is used to insert the contacts into the listbox.

    :param contacts: list
    :param contactsListbox: tk.Listbox

    """

    if len(contacts) == 0:
        contactsListbox.insert("end", "No contacts available.")

    for contact in contacts:
        contactsListbox.insert("end", contact["username"])


def selectAlbum(
    event: callable,
    albunsListbox: Listbox,
    userID: int,
    listAlbumPhotos: Listbox,
    get_user_albuns: callable,
    get_album_photos: callable,
    messagebox: messagebox,
    _albunsProfileWindow_: Toplevel,
):
    """
    This function is used to select an album and place the photos in the listbox.

    :param event: callable
    :param albunsListbox: tk.Listbox
    :param listAlbumPhotos: tk.Listbox
    :param get_user_albuns: callable
    :param get_album_photos: callable
    :param messagebox: tk.messagebox
    :param _albunsProfileWindow_: Toplevel
    """

    # if there is no album selected
    if len(albunsListbox.curselection()) == 0:
        return messagebox.showerror(
            "Error",
            "You need to select an album to view the available photos.",
            parent=_albunsProfileWindow_,
        )

    if albunsListbox.curselection():
        albumName = albunsListbox.get(albunsListbox.curselection())

        # clear the listbox
        listAlbumPhotos.delete(0, "end")

        # inserting the photos in the listbox
        for photo in get_album_photos(
            [
                album["albumID"]
                for album in get_user_albuns(userID)
                if album["name"] == albumName
            ][0]
        ):
            listAlbumPhotos.insert("end", photo["image"])

    # if there is no photos in the album to display
    if listAlbumPhotos.size() == 0:
        listAlbumPhotos.insert("end", "No photos to display.")


def previewSelectedPhoto(
    event: callable,
    listAlbumPhotos: Listbox,
    canvasPreviewImage: Canvas,
    placeholderImage: ImageTk.PhotoImage,
):
    """
    This function is used to preview the selected photo.

    :param event
    :param listAlbumPhotos: tk.Listbox
    :param canvasPreviewImage: Canvas
    :param placeholderImage: ImageTk.PhotoImage
    """

    if listAlbumPhotos.curselection():
        photoName = listAlbumPhotos.get(listAlbumPhotos.curselection())

        currentSelectedImage = ImageTk.PhotoImage(
            Image.open(f"{photoName}").resize((295, 245))
        )

        canvasPreviewImage.create_image(0, 0, image=currentSelectedImage, anchor=NW)

        canvasPreviewImage.image = currentSelectedImage
    else:
        canvasPreviewImage.create_image(0, 0, image=placeholderImage, anchor=NW)


def editAlbumName(
    event: callable,
    albunsListbox: Listbox,
    editAlbumInput: Entry,
    userID: int,
    get_user_albuns: callable,
    edit_album: callable,
    messagebox: messagebox,
    _albunsProfileWindow_: Toplevel,
    get_albuns: callable,
):
    """
    This function is used to edit the album name.

    :param event:
    """

    if len(albunsListbox.curselection()) == 0:
        return messagebox.showerror(
            "Error",
            "You need to select an album to edit the name.",
            parent=_albunsProfileWindow_,
        )

    if editAlbumInput.get() == "":
        return messagebox.showerror(
            "Error",
            "You need to type the new album name.",
            parent=_albunsProfileWindow_,
        )
    # check if the album name already exists with case insensitive
    elif editAlbumInput.get().lower() in [
        album["name"].lower() for album in get_albuns()
    ]:
        return messagebox.showerror(
            "Error",
            "This album name already exists.",
            parent=_albunsProfileWindow_,
        )

    # checking if is trying to edit the same album that was previously edited
    elif editAlbumInput.get() == albunsListbox.get(albunsListbox.curselection()):
        return messagebox.showerror(
            "Error",
            "You need to type a different name.",
            parent=_albunsProfileWindow_,
        )
    else:
        # to get the real index id from the database of the album
        albumID = [
            album["albumID"]
            for album in get_user_albuns(userID)
            if album["name"] == albunsListbox.get(albunsListbox.curselection())
        ][
            0
        ]  # to return the value inside the list eg: [1] -> 1

        edit_album(albumID, editAlbumInput.get())
        editAlbumInput.delete(0, END)
        # clear the listbox
        albunsListbox.delete(0, "end")
        # inserting the albuns in the listbox
        for album in get_user_albuns(userID):
            albunsListbox.insert("end", album["name"])

        messagebox.showinfo(
            "Success",
            "The album name was successfully changed.",
            parent=_albunsProfileWindow_,
        )


def addAlbum(
    event: callable,
    addAlbumInput: Entry,
    userID: int,
    get_user_albuns: callable,
    add_album: callable,
    messagebox: messagebox,
    _albunsProfileWindow_: Toplevel,
    get_albuns: callable,
    albunsListbox: Listbox,
):
    """
    This function is used to add an album.

    :param event:
    """

    if addAlbumInput.get() == "":
        return messagebox.showerror(
            "Error",
            "You need to type the album name.",
            parent=_albunsProfileWindow_,
        )
    # check if the album name already exists with case insensitive
    elif addAlbumInput.get().lower() in [
        album["name"].lower() for album in get_albuns()
    ]:
        return messagebox.showerror(
            "Error",
            "This album name already exists.",
            parent=_albunsProfileWindow_,
        )
    else:
        add_album(addAlbumInput.get(), userID)
        addAlbumInput.delete(0, END)
        # clear the listbox
        albunsListbox.delete(0, "end")
        # inserting the albuns in the listbox
        for album in get_user_albuns(userID):
            albunsListbox.insert("end", album["name"])

        messagebox.showinfo(
            "Success",
            "The album was successfully added.",
            parent=_albunsProfileWindow_,
        )


def removePhoto(
    event: callable,
    listAlbumPhotos: Listbox,
    canvasPreviewImage: Canvas,
    placeholderImage: ImageTk.PhotoImage,
    get_all_photos: callable,
    remove_photo: callable,
    messagebox: messagebox,
    _albunsProfileWindow_: Toplevel,
):
    """
    This function is used to remove a photo from an album.

    :param event:
    """
    if listAlbumPhotos.curselection() == ():
        return messagebox.showerror(
            "Error",
            "You need to select a photo to remove.",
            parent=_albunsProfileWindow_,
        )

    # get the selected photo id from the database
    photoID = [
        photo["photoID"]
        for photo in get_all_photos()
        if photo["image"] == listAlbumPhotos.get(listAlbumPhotos.curselection())
    ][0]

    confirmDelete = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this photo?",
        parent=_albunsProfileWindow_,
    )

    if confirmDelete == True:
        remove_photo(photoID)
        messagebox.showinfo(
            "Success",
            "The photo was successfully deleted.",
            parent=_albunsProfileWindow_,
        )
        # delete the selected photo from the listbox
        listAlbumPhotos.delete(listAlbumPhotos.curselection())
        # checking if there is no photos in the album after deleting one
        if listAlbumPhotos.size() == 0:
            listAlbumPhotos.insert("end", "No photos to display.")
        canvasPreviewImage.create_image(0, 0, image=placeholderImage, anchor=NW)
    else:
        return


def selectFavoriteAlbum(
    event: callable,
    favoritesAlbunsListbox: Listbox,
    photosListbox: Listbox,
    userID: int,
    get_favorites_albuns: callable,
    get_album_photos: callable,
    messagebox: messagebox,
    _favoritesProfileWindow_: Toplevel,
    selectedAlbum: str,
    current_index: int,
):
    # if there is no album selected
    if len(favoritesAlbunsListbox.curselection()) == 0:
        return messagebox.showerror(
            "Error",
            "You need to select an album to view the available photos.",
            parent=_favoritesProfileWindow_,
        )

    if favoritesAlbunsListbox.curselection():
        selectedAlbum = favoritesAlbunsListbox.get(
            favoritesAlbunsListbox.curselection()
        )

        # clear the listbox
        photosListbox.delete(0, "end")

        # inserting the photos in the listbox
        for photo in get_album_photos(
            [
                album["albumID"]
                for album in get_favorites_albuns(userID)
                if album["name"] == selectedAlbum
            ][0]
        ):
            photosListbox.insert("end", photo["image"])

    # if there is no photos in the album to display
    if photosListbox.size() == 0:
        photosListbox.insert("end", "No photos to display.")
