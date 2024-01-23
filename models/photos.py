from classes.Photo import Photo
from classes.User import User
from classes.Category import Category


def get_photos() -> list:
    """
    Function to get the photos

    :return: list
    """
    photos = Photo().get_photos()

    return photos


def get_filtered_photos(category: str, username: str) -> list:
    """
    Function to get the filtered photos by category or user

    :parm category: str
    :parm username: str
    """

    photos = Photo().get_photos()

    categories = Category().get_categories()

    users = User().get_users()

    if category != "all":
        # returning photos by category
        return [
            {
                **photo,
                "category": next(
                    filter(
                        lambda category: category["categoryID"] == photo["categoryID"],
                        categories,
                    )
                )["name"],
            }
            for photo in photos
            if next(
                filter(
                    lambda category: category["categoryID"] == photo["categoryID"],
                    categories,
                )
            )["name"]
            == category
        ]

    if category == "all":
        # returing all photos excluding the user info and with the category name instead of the categoryID
        return [
            {
                **photo,
                "category": next(
                    filter(
                        lambda category: category["categoryID"] == photo["categoryID"],
                        categories,
                    )
                )["name"],
                "user": next(
                    filter(lambda user: user["userID"] == photo["userID"], users)
                )["username"],
            }
            for photo in photos
        ]

    # filtering by username
    return [
        {
            **photo,
            "category": next(
                filter(
                    lambda category: category["categoryID"] == photo["categoryID"],
                    categories,
                )
            )["name"],
            "user": next(filter(lambda user: user["userID"] == photo["userID"], users))[
                "username"
            ],
        }
        for photo in photos
        if next(filter(lambda user: user["userID"] == photo["userID"], users))[
            "username"
        ]
        == username
    ]


def get_album_photos(albumID: int = 0) -> list:
    """
    Function to get the album photos

    :param albumID: int

    :return: list
    """
    photos = Photo().get_photos()

    return (
        photos
        if albumID == 0
        else [photo for photo in photos if photo["albumID"] == albumID]
    )


def remove_photo(photoID: int) -> bool:
    """
    Function to delete a photo

    :param photoID: int

    :return: bool
    """
    photos = Photo().get_photos()

    for photo in photos:
        if photo["photoID"] == photoID:
            Photo(
                photo["photoID"],
            ).delete_photo()
            return True
    return False


def get_all_photos() -> list:
    """
    Function to get all photos

    :return: list
    """
    photos = Photo().get_photos()

    return photos


def get_photo(photoID: int) -> dict:
    """
    Function to get a photo detail

    :param photoID: int

    :return: dict
    """
    photos = Photo().get_photos()

    for photo in photos:
        if photo["photoID"] == photoID:
            photo = Photo(
                photo["photoID"],
                photo["description"],
                photo["publishedDate"],
                photo["image"],
                photo["likes"],
                photo["views"],
                photo["rating"],
                photo["categoryID"],
                photo["albumID"],
            ).get_photos()

        # returning the category name instead of the categoryID and the username instead of the userID
        return {
            **photo,
            "category": Category(photo["categoryID"]).get_categories()["name"],
            "user": User(photo["userID"]).get_users()["username"],
        }


def add_photo(description: str, publishedDate: str, image: str, category: str) -> bool:
    """
    Function to add a photo

    :param description: str
    :param image: str
    :param categoryID: int
    :param albumID: int
    :param userID: int

    :return: bool
    """
    photos = Photo().get_photos()

    categories = Category().get_categories()

    for category in categories:
        if category["name"] == category:
            categoryID = category["categoryID"]

    photo = Photo(
        description=description,
        publishedDate=publishedDate,
        image=image,
        categoryID=categoryID,
    ).add_photo()

    return True
