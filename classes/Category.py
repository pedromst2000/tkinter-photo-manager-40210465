from database import Database


class Category:
    # attributes
    categoryID = 0
    category = ""

    # constructor
    def __init__(
        self,
        categoryID: int = 0,
        category: str = "",
    ) -> None:
        """
        constructor of the Class Category

        optional fields if nothing is passed, the default value is used

        :param category: str (optional, default="")


        :return: None
        """

        self.categoryID = categoryID
        self.category = category

    # methods

    def get_categories(self) -> list:
        """
        Method to get all instances of the Class Category

        :return: list

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
        categories = db.get_categories()
        return categories

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
