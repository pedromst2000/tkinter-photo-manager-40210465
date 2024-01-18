from database import Database


class Favorite:
    # attributes
    albumID = 0
    userID = 0

    # constructor
    def __init__(
        self,
        albumID: int = 0,
        userID: int = 0,
    ) -> None:
        """
        constructor of the Class Favorite

        optional fields if nothing is passed, the default value is used

        :param albumID: int (optional, default=0)
        :param userID: int (optional, default=0)

        :return: None
        """

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

    def delete_favorite(self):
        """
        Method to delete an instance of the Class Favorite
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

        db.delete_favorite(self)
