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


def checkLoggedUserRole(email: str) -> str:
    """
    Function to check the role of the logged user

    :param email: str

    :return: str

    """
    db = Database(users=[], categories=[], photos=[], comments=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:  # if the email exists in the database
            return user["role"]  # return the role of the user

    return None  # if the email doesn't exist in the database, return None


def checkLoggedUserIsBlocked(email: str) -> bool:
    """
    Function to check if the logged user is blocked

    :param email: str

    :return: bool

    """

    db = Database(users=[], categories=[], photos=[], comments=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:  # if the email exists in the database
            return user["isBlocked"]  # return the isBlocked value of the user

    return None  # if the email doesn't exist in the database, return None


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
        "regular",
        "assets/images/profile_avatars/default_avatar.jpg",
        False,
    )
    user.add_user()  # add new instance of the user to the database

    return True  # return True if the user was created successfully


# Checking if the username or email is unique
def checkUnique(username: str, email: str) -> bool:
    """
    Function to check if the username or email is unique

    :param username: str
    :param email: str

    :return: bool

    """
    db = Database(users=[], categories=[], photos=[], comments=[])
    users = db.get_users()

    username = username.lower()  # convert the username to lowercase
    email = email.split("@")[0].lower()  # convert the email to lowercase

    email = "@".join(email)  # join the email back together

    for user in users:
        if user["username"].lower() == username or user["email"].lower() == email:
            return False  # if the username or email already exists, return False

    return True  # if the username and email are unique, return True


def get_logged_user(email: str) -> User:
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


def save_avatar(email: str, avatar: str) -> bool:
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


def change_password(email: str, newPassword: str) -> bool:
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


def delete_account(email: str) -> bool:
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
