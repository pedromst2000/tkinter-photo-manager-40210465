from database import Database


class Album:
    # attributes
    name = ""
    creatorID = 0

    # constructor
    def __init__(
        self,
        name: str = "",
        creatorID: int = 0,
    ) -> None:
        """
        constructor of the Class Album

        optional fields if nothing is passed, the default value is used

        :param name: str (optional, default="")
        :param creatorID: int (optional, default=0)

        :return: None
        """

        self.name = name
        self.creatorID = creatorID

    # methods

    def get_albuns(self):
        """
        Method to get all instances of the Class Album

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        return db.get_albuns()

    def add_album(self):
        """
        Method to add new instance of the Class Aalbum

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        db.create_album(self)

    def update_album(self):
        """
        Method to update an instance of the Class Album

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        db.update_album(self)
