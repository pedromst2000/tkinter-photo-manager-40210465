from classes.Favorite import Favorite
from classes.Album import Album


def get_favorites_albuns(userID: int) -> list:
    """
    Function to get the user favorites albums

    :param userID: int

    :return: list
    """

    favorites = Favorite().get_favorites()
    albuns = Album().get_albuns()

    # aggregating the data between the favorites and albuns to get the name of the album
    return [
        {"albumID": favorite["albumID"], "name": album["name"]}
        for favorite in favorites
        for album in albuns
        if favorite["userID"] == userID and favorite["albumID"] == album["albumID"]
    ]
