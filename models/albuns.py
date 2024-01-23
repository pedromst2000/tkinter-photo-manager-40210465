from classes.Album import Album


def get_albuns() -> list:
    """
    Function to get all albuns

    :return: list
    """
    return Album().get_albuns()


def get_user_albuns(userID: int) -> list:
    """
    Function to get the user albums

    :param userID: int

    :return: list
    """

    albums = Album(
        albumID=None,
        name=None,
        creatorID=None,
    ).get_albuns()

    # returing only the albums of the user
    return [album for album in albums if album["creatorID"] == userID]


def edit_album(albumID: int, new_album_name: str) -> bool:
    """
    Function to change the name of the album

    :parm albumID: int
    :param new_album_name: str

    :return: bool
    """

    albuns = Album().get_albuns()

    for album in albuns:
        if album["albumID"] == albumID:
            album["name"] = new_album_name
            album = Album(
                album["albumID"],
                album["name"],
                album["creatorID"],
            ).update_album(album)

            return True
    return False


def add_album(name: str, creatorID: int) -> bool:
    """
    Function to add a new album

    :param name: str
    :param creatorID: int

    :return: bool
    """
    album = Album(
        albumID=None,
        name=name,
        creatorID=creatorID,
    ).add_album()

    return True if album else False
