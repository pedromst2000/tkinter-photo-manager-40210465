from classes.Photo import Photo


def get_album_photos(albumID: int = 0) -> list:
    """
    Function to get the album photos

    :param albumID: int

    :return: list
    """
    photos = Photo().get_photos()

    return (
        photos
        if albumID == 0
        else [photo for photo in photos if photo["albumID"] == albumID]
    )


def remove_photo(photoID: int) -> bool:
    """
    Function to delete a photo

    :param photoID: int

    :return: bool
    """
    photos = Photo().get_photos()

    for photo in photos:
        if photo["photoID"] == photoID:
            Photo(
                photo["photoID"],
            ).delete_photo()
            return True
    return False


def get_all_photos() -> list:
    """
    Function to get all photos

    :return: list
    """
    photos = Photo().get_photos()

    return photos


def get_photo(photoID: int) -> dict:
    """
    Function to get a photo detail

    :param photoID: int

    :return: dict
    """
    photos = Photo().get_photos()

    for photo in photos:
        if photo["photoID"] == photoID:
            photo = Photo(
                photo["photoID"],
                photo["description"],
                photo["publishedDate"],
                photo["image"],
                photo["likes"],
                photo["views"],
                photo["rating"],
                photo["categoryID"],
                photo["albumID"],
            ).get_photos()

            return photo
    return {}
