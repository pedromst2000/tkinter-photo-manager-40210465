from database import Database
from classes.User import User


def login(email: str, password: str) -> User:
    """
    Function to login a user

    :param email: str
    :param password: str

    :return: User
    """

    # the class Database takes a list of users as a parameter since the constructor takes a list of users as a parameter (self, users)
    db = Database(users=[], categories=[], photos=[], comments=[])
    users = db.get_users()

    for user in users:
        # check if the email exists
        if user["email"] == email:
            # check if the password is correct
            if user["password"] == password:
                return user
            else:
                return None  # if the password is incorrect, return None

    return None  # if the email doesn't exist, return None


# add a new user to the database
def register(
    username: str,
    email: str,
    password: str,
) -> bool:
    """
    Function to register a new user

    :param username: str
    :param email: str
    :param password: str

    :return: bool

    """
    # if the email and the username doesn't exist, create the user
    user = User(
        username,
        email,
        password,
        "unsigned",
        "assets/images/profile_avatars/default_avatar.jpg",
        False,
    )
    user.add_user()  # add new instance of the user to the database

    return True  # return True if the user was created successfully


def checkSignUpUsername(username: str) -> bool:
    """
    Function to check if the username is unique

    :param username: str

    :return: bool

    """
    db = Database(users=[], categories=[], photos=[], comments=[])
    users = db.get_users()

    # validation for comparing with case insensitive usernames :

    #  Not accepting case insensitive usernames
    # => PEDROMST = pedromst  - will be the same

    _username_ = username.lower()  # to make the username case insensitive

    for user in users:
        if user["username"].lower() == _username_:
            return False  # return False if the username isn't unique

    return True  # return True if the username is unique


def checkSignUpEmail(email: str) -> bool:
    """
    Function to check if the email is unique

    :param email: str

    :return: bool

    """

    db = Database(users=[], categories=[], photos=[], comments=[])
    users = db.get_users()

    # validation for comparing with case insensitive emails :

    #  Not accepting case insensitive emails
    # => PEDROMST@GMAIL.COM = pedromst@gmail.com  - will be the same

    local_part, domain_part = email.split("@")
    local_part = local_part.lower()  # Convert the entire local part to lowercase

    _email_ = f"{local_part}@{domain_part}"

    for user in users:
        if user["email"].lower() == _email_.lower():
            return False  # return False if the email isn't unique

    return True  # return True if the email is unique


def getUserInfo(email: str) -> User:
    """
    Function to get the logged user information (payload)

    :param email: str

    :return: User

    """

    db = Database(users=[], categories=[], photos=[], comments=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:
            return user

    return None


def saveAvatar(email: str, avatar: str) -> bool:
    """
    Function to save the avatar of the user

    :param email: str
    :param avatar: str

    :return: bool

    """

    db = Database(users=[], categories=[], photos=[], comments=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:  # if the email exists in the database
            user[
                "avatar"
            ] = f"assets/images/Profile/{avatar}"  # update the avatar of the user
            user = User(
                user["username"],
                user["email"],
                user["password"],
                user["role"],
                user["avatar"],
                user["isBlocked"],
            )
            user.update_user()  # update the user in the database
            return True  # return True if the avatar was updated successfully

    return False  # return False if the avatar wasn't updated successfully


def changePassword(email: str, newPassword: str) -> bool:
    """
    Function to change the password of the user

    :param email: str
    :param newPassword: str

    :return: bool

    """

    db = Database(users=[], categories=[], photos=[], comments=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:  # if the email exists in the database
            user["password"] = newPassword  # update the password of the user
            user = User(
                user["username"],
                user["email"],
                user["password"],
                user["role"],
                user["avatar"],
                user["isBlocked"],
            )
            user.update_user()  # update the user in the database
            return True  # return True if the password was updated successfully

    return False  # return False if the password wasn't updated successfully


def deleteAccount(email: str) -> bool:
    """
    Function to delete the account of the user

    :param email: str

    :return: bool

    """

    db = Database(users=[], categories=[], recipes=[], ingredients=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:  # if the email exists in the database
            user = User(
                user["username"],
                user["email"],
                user["password"],
                user["role"],
                user["avatar"],
                user["isBlocked"],
            )
            user.delete_user()  # delete the user from the database
            return True  # return True if the user was deleted successfully

    return False  # return False if the user wasn't deleted successfully
