from database import Database


class Favorite:
    # attributes
    favoriteID = 0
    albumID = 0
    userID = 0

    # constructor
    def __init__(
        self,
        favoriteID: int = 0,
        albumID: int = 0,
        userID: int = 0,
    ) -> None:
        """
        constructor of the Class Favorite

        optional fields if nothing is passed, the default value is used

        :param favoriteID: int (optional, default=0)
        :param albumID: int (optional, default=0)
        :param userID: int (optional, default=0)

        :return: None
        """

        self.favoriteID = favoriteID
        self.albumID = albumID
        self.userID = userID

    # methods

    def get_favorites(self):
        """
        Method to get all instances of the Class Favorite

        :return: None

        """

        db = Database(
            users=[],
            categories=[],
            photos=[],
            comments=[],
            albuns=[],
            favorites=[],
            contacts=[],
        )
        return db.get_favorites()

    def add_favorite(self):
        """
        Method to add new instance of the Class Favorite

        :return: None

        """

        db = Database(
            users=[],
            categories=[],
            photos=[],
            comments=[],
            albuns=[],
            favorites=[],
            contacts=[],
        )
        db.create_favorite(self)
