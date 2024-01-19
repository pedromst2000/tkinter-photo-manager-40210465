from classes.Category import Category


def get_categories() -> list:
    """
    Function to get the categories

    :return: list
    """

    categories = Category().get_categories()

    # return only the category name
    return [category["category"] for category in categories]


def add_category(categoryName: str) -> bool:
    """
    Function to add a category

    :param categoryName: str

    :return: bool
    """

    categories = Category().get_categories()

    for category in categories:
        # check if the category already exists with case insensitive
        if category["category"].lower() == categoryName.lower():
            return False

    Category(category["categoryID"], categoryName).add_category()

    return True


def delete_category(categoryName: str) -> bool:
    """
    Function to delete a category

    :param categoryID: int

    :return: bool

    """

    categories = Category().get_categories()

    for category in categories:
        if category["category"] == categoryName:
            category = Category(
                category["categoryID"],
                category["category"],
            )
            category.delete_category()

            return True  # return True if the category was deleted successfully

    return False  # return False if the category wasn't deleted successfully
