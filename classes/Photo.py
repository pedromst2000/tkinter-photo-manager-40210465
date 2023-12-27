from database import Database


class Photo:
    # attributes
    photoID = 0
    description = ""
    publishedDate = ""
    image = ""
    likes = 0
    rating = 0
    categoryID = 0
    creatorID = 0

    # constructor
    def __init__(
        self,
        description: str,
        publishedDate: str,
        image: str,
        likes: int,
        rating: int,
        categoryID: int,
        creatorID: int,
    ) -> None:
        """
        Constructor of the Class Photo

        :param description: str
        :param publishedDate: str
        :param image: str
        :param likes: int
        :param rating: int
        :param categoryID: int
        :param creatorID: int

        :return: None
        """

        self.description = description
        self.publishedDate = publishedDate
        self.image = image
        self.likes = likes
        self.rating = rating
        self.categoryID = categoryID
        self.creatorID = creatorID

    # methods
    def add_photo(self):
        """
        Method to add new instance of the Class Photo

        :return: None

        """

        db = Database(users=[], categories=[], photos=[], comments=[])
        db.create_photo(self)

    def update_photo(self):
        """
        Method to update an instance of the Class Photo

        :return: None

        """

        db = Database(users=[], categories=[], photos=[], comments=[])
        db.update_photo(self)

    def delete_photo(self):
        """
        Method to delete an instance of the Class Photo

        :return: None

        """

        db = Database(users=[], categories=[], photos=[], comments=[])
        db.delete_photo(self)
