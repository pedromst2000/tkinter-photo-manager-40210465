from database import Database


class Category:
    # attributes
    category = ""

    # constructor
    def __init__(
        self,
        category: str = "",
    ) -> None:
        """
        constructor of the Class Category

        optional fields if nothing is passed, the default value is used

        :param category: str (optional, default="")


        :return: None
        """

        self.category = category

    # methods
    def add_category(self):
        """
        Method to add new instance of the Class Category

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
        db.create_category(self)

    def delete_category(self):
        """
        Method to delete an instance of the Class Category

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
        db.delete_category(self)
