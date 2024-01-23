from database import Database


class Contact:
    # attributes
    contactID = 0
    title = ""
    message = ""
    userID = 0

    # constructor
    def __init__(self, contactID: int, title: str, message: str, userID: int) -> None:
        """
        constructor of the Class Contact

        :param contactID: int
        :param title: str
        :param message: str
        :param userID: int

        :return: None
        """

        self.contactID = contactID
        self.title = title
        self.message = message
        self.userID = userID

    # methods

    def get_contacts(self):
        """
        Method to get all instances of the Class Contact

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
        return db.get_contacts()

    def add_contact(self):
        """
        Method to add new instance of the Class Contact

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
        db.create_contact(self)
