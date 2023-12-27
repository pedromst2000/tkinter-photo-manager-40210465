from database import Database


class User:
    # attributes
    username = ""
    email = ""
    password = ""
    avatar = ""
    role = ""
    isBlocked = False

    # constructor
    def __init__(
        self,
        username: str,
        email: str,
        password: str,
        role: str,
        avatar: str,
        isBlocked: bool,
    ) -> None:
        """

        Constructor of the Class User

        :param username: str
        :param email: str
        :param password: str
        :param role: str
        :param avatar: str
        :param isBlocked: bool

        :return: None

        """

        self.username = username
        self.email = email
        self.password = password
        self.avatar = avatar
        self.role = role
        self.isBlocked = isBlocked

    # methods
    def add_user(self):
        """
        Method to add new instance of the Class User

        :return: None

        """

        db = Database(users=[], categories=[], photos=[], comments=[])
        db.create_user(self)

    def update_user(self):
        """
        Method to update an instance of the Class User

        :return: None

        """

        db = Database(users=[], categories=[], photos=[], comments=[])
        db.update_user(self)

    def delete_user(self):
        """
        Method to delete an instance of the Class User

        :return: None

        """

        db = Database(users=[], categories=[], photos=[], comments=[])
        db.delete_user(self)
