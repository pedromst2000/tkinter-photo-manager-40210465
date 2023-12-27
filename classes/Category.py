from database import Database


class Category:
    # attributes
    category = ""

    # constructor
    def __init__(
        self,
        category: str,
    ) -> None:
        """
        constructor of the Class Category

        :param category: str

        :return: None
        """

        self.category = category

    # methods
    def add_category(self):
        """
        Method to add new instance of the Class Category

        :return: None

        """

        db = Database(users=[], categories=[], photos=[], comments=[])
        db.create_category(self)

    def delete_category(self):
        """
        Method to delete an instance of the Class Category

        :return: None

        """

        db = Database(users=[], categories=[], photos=[], comments=[])
        db.delete_category(self)
