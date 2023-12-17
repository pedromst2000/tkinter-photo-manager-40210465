from database import *


def login(email: str, password: str) -> dict:
    """
    This function is used to login the user.

    :param email: The email of the user. (required)
    :param password: The password of the user. (required)

    :return: The user object.
    """

    db_init = init()

    db_users = db_init["get_users"]()  # get the users from the database

    for user in db_users:
        # Checking if the email exits
        if user["email"] == email:
            # Checking if the password is correct
            if user["password"] == password:
                return user
            else:
                return False  # if the password is incorrect

        return False  # if the email is incorrect


def checkLoggedUserRole(email: str) -> dict:
    """
    This function is used to check the role of the logged in user.

    :param email: The email of the user. (required)

    :return: The user object.
    """

    db_init = init()

    db_users = db_init["get_users"]()  # get the users from the database

    for user in db_users:
        # Checking if the email exits
        if user["email"] == email:
            return user["role"]  # return the role of the user

    return False  # if the email is incorrect


def checkLoggedUserIsBlocked(email: str) -> dict:
    """
    This function is used to check if the logged in user is blocked.

    :param email: The email of the user. (required)

    :return: The user object.
    """

    db_init = init()

    db_users = db_init["get_users"]()  # get the users from the database

    for user in db_users:
        if user["email"] == email:  # if the email exists in the database
            return user["isBlocked"]  # return the isBlocked value of the user

    return None  # if the email doesn't exist in the database, return None


def register(username: str, email: str, password: str) -> dict:
    """
    This function is used to register the user.

    :param username: The username of the user. (required)
    :param email: The email of the user. (required)
    :param password: The password of the user. (required)

    :return: The user object.
    """

    db_init = init()

    db_users = db_init["get_users"]()  # get the users from the database

    username = username.lower()  # to make the username case insensitive
    email = email.lower()  # to make the email case insensitive

    for user in db_users:
        # Checking if the username or email already exists
        if user["username"] == username or user["email"] == email:
            return False  # if the username or email already exists

    # if the username or email doesn't exist, create a new user
    db_init["create_user"](username, email, password)

    return True  # return True if the user is created


def changePassword(email: str, newPassword: str) -> dict:
    """
    This function is used to change the password of the user.

    :param email: The email of the user. (required)
    :param newPassword: The new password of the user. (required)

    :return: The user object.
    """

    db_init = init()

    db_users = db_init["get_users"]()  # get the users from the database

    for user in db_users:
        # Checking if the email exits
        if user["email"] == email:
            user["password"] = newPassword

            db_init["update_user"](
                user["id"],
                user["username"],
                user["email"],
                user["password"],
                user["role"],
                user["isBlocked"],
            )

            return True  # return True if the password is changed

    return False  # return False if the email doesn't exist


def changeAvatar(email: str, newAvatar: str) -> dict:
    """
    This function is used to change the avatar of the user.

    :param email: The email of the user. (required)
    :param newAvatar: The new avatar of the user. (required)

    :return: The user object.
    """

    db_init = init()

    db_users = db_init["get_users"]()  # get the users from the database

    for user in db_users:
        # Checking if the email exits
        if user["email"] == email:
            user["avatar"] = newAvatar

            db_init["update_user"](
                user["id"],
                user["username"],
                user["email"],
                user["password"],
                user["role"],
                user["isBlocked"],
                user["avatar"],
            )

            return True  # return True if the avatar is changed

    return False  # return False if the email doesn't exist


def deleteAccount(email: str) -> dict:
    """
    This function is used to delete the account of the user.

    :param email: The email of the user. (required)

    :return: The user object.
    """

    db_init = init()

    db_users = db_init["get_users"]()  # get the users from the database

    for user in db_users:
        # Checking if the email exits
        if user["email"] == email:
            db_init["delete_user"](user["id"])

            return True  # return True if the account is deleted

    return False  # return False if the email doesn't exist