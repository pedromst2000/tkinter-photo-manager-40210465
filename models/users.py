from classes.User import User


def login(email: str, password: str) -> User:
    """
    Function to login a user

    :param email: str
    :param password: str

    :return: User
    """

    # accessing the Class User and calling the method get_users()
    users = User().get_users()

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
    User(
        userID=0,
        username=username,
        email=email,
        password=password,
        avatar="assets/images/profile_avatars/default_avatar.jpg",
        role="unsigned",
        followers=0,
        photos=0,
        isBlocked=False,
    ).add_user()  # add new instance of the user to the database

    return True  # return True if the user was created successfully


def checkSignUpUsername(username: str) -> bool:
    """
    Function to check if the username is unique

    :param username: str

    :return: bool

    """

    users = User().get_users()

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

    users = User().get_users()

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


def getUserInfo(userID: int) -> User:
    """
    Function to get the logged user information (payload)

    :param userID: int

    :return: User

    """

    users = User().get_users()

    for user in users:
        if user["userID"] == userID:
            return user

    return None


def findUserID(email: str) -> int:
    """
    Function to find the id of the user by its email

    :param email: str

    :return userID: int

    """

    users = User().get_users()

    for user in users:
        if user["email"] == email:
            return user["userID"]

    return None


def saveAvatar(userID: int, avatar: str) -> bool:
    """
    Function to save the avatar of the user

    :param userID: int
    :param avatar: str

    :return: bool

    """

    users = User().get_users()

    for user in users:
        if user["userID"] == userID:  # if the email exists in the database
            user[
                "avatar"
            ] = f"assets/images/Profile/{avatar}"  # update the avatar of the user
            User(
                user["avatar"],
            ).update_user()  # update the user in the database

            return True  # return True if the avatar was updated successfully

    return False  # return False if the avatar wasn't updated successfully


def changePassword(userID: int, newPassword: str) -> bool:
    """
    Function to change the password of the user

    :param userID: int
    :param newPassword: str

    :return: bool

    """

    users = User().get_users()

    for user in users:
        if user["userID"] == userID:  # if the email exists in the database
            user["password"] = newPassword  # update the password of the user
            User(
                user["password"],
            ).update_user()  # update the user in the database

            return True  # return True if the password was updated successfully

    return False  # return False if the password wasn't updated successfully


def get_users_list() -> list:
    """
    Function to get the list of all users with partial information :

    userID, username, email and role

    :return: list

    """
    return [
        {
            "userID": user["userID"],
            "username": user["username"],
            "email": user["email"],
            "role": user["role"],
            "isBlocked": user["isBlocked"],
        }
        for user in User().get_users()
        if user["role"] != "admin"
    ]


def change_role(username: str, new_role: str) -> bool:
    """
    Function to change the role of the user

    :param username: str
    :param new_role: str

    :return: bool
    """

    users = User().get_users()

    for user in users:
        if user["username"] == username:
            user["role"] = new_role
            user = User(
                user["userID"],
                user["username"],
                user["email"],
                user["password"],
                user["avatar"],
                user["role"],
                user["followers"],
                user["photos"],
                user["isBlocked"],
            )
            user.update_user()
            return True
    return False


def block_user(username: str) -> bool:
    """
    Function to block the user

    :param username: str

    :return: bool

    """

    users = User().get_users()

    for user in users:
        if user["username"] == username:
            user["isBlocked"] = True  # update the isBlocked of the user
            user = User(
                user["userID"],
                user["username"],
                user["email"],
                user["password"],
                user["avatar"],
                user["role"],
                user["followers"],
                user["photos"],
                user["isBlocked"],
            )
            user.update_user()
            return True

    return False  # return False if the user wasn't blocked successfully


def unblock_user(username: str) -> bool:
    """
    Function to unblock the user

    :param username: str

    :return: bool

    """

    users = User().get_users()

    for user in users:
        if user["username"] == username:
            user["isBlocked"] = False  # update the isBlocked of the user
            user = User(
                user["userID"],
                user["username"],
                user["email"],
                user["password"],
                user["avatar"],
                user["role"],
                user["followers"],
                user["photos"],
                user["isBlocked"],
            )
            user.update_user()
            return True

    return False  # return False if the user wasn't unblocked successfully


def filter_users(username: str, email: str) -> list:
    """
    Function to filter the users by username and email

    :param username: str
    :param email: str

    :return: list

    """

    users = User().get_users()

    # Admin cannot be filtered
    filteredUsers = [user for user in users if user["role"] != "admin"]

    # filter by username
    if username != "":
        filteredUsers = [
            user
            for user in filteredUsers
            if user["username"].lower().startswith(username.lower())
        ]

    # filter by email
    if email != "":
        filteredUsers = [
            user
            for user in filteredUsers
            if user["email"].lower().startswith(email.lower())
        ]

    # filter by username and email
    if username != "" and email != "":
        filteredUsers = [
            user
            for user in filteredUsers
            if user["username"].lower().startswith(username.lower())
            and user["email"].lower().startswith(email.lower())
        ]

    return filteredUsers
