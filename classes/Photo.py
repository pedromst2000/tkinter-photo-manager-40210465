from database import Database


class Photo:
    # attributes
    photoID = 0
    description = ""
    publishedDate = ""
    image = ""
    likes = 0
    views = 0
    rating = 0
    categoryID = 0
    creatorID = 0

    # constructor
    def __init__(
        self,
        description: str = "",
        publishedDate: str = "",
        image: str = "",
        likes: int = 0,
        views: int = 0,
        rating: int = 0,
        categoryID: int = 0,
        creatorID: int = 0,
    ) -> None:
        """
        Constructor of the Class Photo

        optional fields if nothing is passed, the default value is used

        :param description: str (optional, default="")
        :param publishedDate: str (optional, default="")
        :param image: str (optional, default="")
        :param likes: int (optional, default=0)
        :param views: int (optional, default=0)
        :param rating: int (optional, default=0)
        :param categoryID: int (optional, default=0)
        :param creatorID: int (optional, default=0)

        :return: None
        """

        self.description = description
        self.publishedDate = publishedDate
        self.image = image
        self.likes = likes
        self.views = views
        self.rating = rating
        self.categoryID = categoryID
        self.creatorID = creatorID

    # methods

    def get_photos(self):
        """
        Method to get all instances of the Class Photo

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        return db.get_photos()

    def add_photo(self):
        """
        Method to add new instance of the Class Photo

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        db.create_photo(self)

    def update_photo(self):
        """
        Method to update an instance of the Class Photo

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        db.update_photo(self)

    def delete_photo(self):
        """
        Method to delete an instance of the Class Photo

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        db.delete_photo(self)
