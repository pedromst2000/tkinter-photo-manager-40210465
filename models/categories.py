from classes.Category import Category
from classes.Photo import Photo
from database import Database


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
    photos = Photo().get_photos()

    for category in categories:
        if category["category"] == categoryName:
            category = Category(
                category["categoryID"],
                category["category"],
            )
            category.delete_category()

            # finding the id of the category by the name of the category
            categoryID = [
                category["categoryID"]
                for category in categories
                if category["category"] == categoryName
            ][0]
            # removing the photos associated with the category
            for photo in photos:
                photo_ids_to_delete = [
                    photo["photoID"]
                    for photo in photos
                    if photo["categoryID"] == categoryID
                ]

            Database().delete_photos_onCascade(*photo_ids_to_delete)

    return True
