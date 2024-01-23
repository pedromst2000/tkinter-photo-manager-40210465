from database import Database


class Album:
    # attributes
    albumID = 0
    name = ""
    creatorID = 0

    # constructor
    def __init__(self, albumID: int = 0, name: str = "", creatorID: int = 0):
        """
        constructor of the Class Album

        optional params: albumID, name, creatorID (default=None)

        :param albumID: int
        :param name: str
        :param creatorID: int

        """

        self.albumID = albumID
        self.name = name
        self.creatorID = creatorID

    # methods

    def get_albuns(self):
        """
        Method to get all instances of the Class Album

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
        return db.get_albuns()

    def add_album(self):
        """
        Method to add new instance of the Class Aalbum

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
        db.create_album(self)

    def update_album(self, updated_album: dict):
        """
        Method to update an instance of the Class Album

        :param albumID: int
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
        db.update_album(self, updated_album)
