from database import Database


class Comment:
    # attributes
    commentID = 0
    authorID = 0
    comment = ""
    photoID = 0

    # constructor
    def __init__(
        self,
        commentID: int = 0,
        authorID: int = 0,
        comment: str = "",
        photoID: int = 0,
    ) -> None:
        """
        constructor of the Class Comment

        optional fields if nothing is passed, the default value is used

        :param commentID: int (optional, default=0)
        :param authorID: int (optional, default=0)
        :param comment: str (optional, default="")
        :param photoID: int (optional, default=0)

        :return: None
        """

        self.commentID = commentID
        self.authorID = authorID
        self.comment = comment
        self.photoID = photoID

    # methods

    def get_comments(self):
        """
        Method to get all instances of the Class Comment

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
        return db.get_comments()

    def add_comment(self):
        """
        Method to add new instance of the Class Comment

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
        db.create_comment(self)
