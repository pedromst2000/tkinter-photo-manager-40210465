from database import Database


class User:
    # attributes
    username = ""
    email = ""
    password = ""
    avatar = ""
    role = ""
    followers = 0
    isBlocked = False

    # constructor
    def __init__(
        self,
        username: str = "",
        email: str = "",
        password: str = "",
        role: str = "",
        followers: int = 0,
        avatar: str = "",
        isBlocked: bool = False,
    ) -> None:
        """

        Constructor of the Class User

        optional fields if nothing is passed, the default value is used

        :param username: str (optional, default="")
        :param email: str (optional, default="")
        :param password: str (optional, default="")
        :param role: str (optional, default="")
        :param followers: int (optional, default=0)
        :param avatar: str (optional, default="")
        :param isBlocked: bool (optional, default=False)

        :return: None

        """

        self.username = username
        self.email = email
        self.password = password
        self.avatar = avatar
        self.role = role
        self.followers = followers
        self.isBlocked = isBlocked

    # methods

    def get_users(self):
        """
        Method to get all instances of the Class User

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        return db.get_users()

    def add_user(self):
        """
        Method to add new instance of the Class User

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        db.create_user(self)

    def update_user(self):
        """
        Method to update an instance of the Class User

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        db.update_user(self)

    def delete_user(self):
        """
        Method to delete an instance of the Class User

        :return: None

        """

        db = Database(
            users=[], categories=[], photos=[], comments=[], albuns=[], favorites=[]
        )
        db.delete_user(self)
