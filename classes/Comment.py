from database import Database


class Comment:
    # attributes
    authorID = 0
    comment = ""
    photoID = 0

    # constructor
    def __init__(
        self,
        authorID: int,
        comment: str,
        photoID: int,
    ) -> None:
        """
        constructor of the Class Comment

        :param authorID: int
        :param comment: str
        :param photoID: int

        :return: None
        """

        self.authorID = authorID
        self.comment = comment
        self.photoID = photoID

    # methods
    def add_comment(self):
        """
        Method to add new instance of the Class Comment

        :return: None

        """

        db = Database(users=[], categories=[], photos=[], comments=[])
        db.create_comment(self)
