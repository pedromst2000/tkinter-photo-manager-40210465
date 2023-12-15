def init(
    users: list = [], categories: list = [], photos: list = [], comments: list = []
) -> None:
    """
    Initialize the database with the given data.

    :param users: A list of user objects representing the users in the database.
    :param categories: A list of category objects representing the categories in the database.
    :param photos: A list of photo objects representing the photos in the database.
    :param comments: A list of comment objects representing the comments in the database.

    :return: None
    """
    global _users_, _categories_, _photos_, _comments_
    _users_ = users
    _categories_ = categories
    _photos_ = photos
    _comments_ = comments

    def get_users() -> list:
        """
        Retrieve user data from 'users.txt' and return a list of user objects.

        Each user object includes:
        - userID: Unique identifier (int).
        - username: User's username (str).
        - email: User's email address (str).
        - password: User's password (str).
        - avatar: File path or URL for user's avatar (str).
        - role: User's role ('admin', 'regular', 'unsigned') (str).
        - isBlocked: Indicates if the user is blocked (bool).

        :return: List of user objects representing the users in the database.
        """

        file = open("files/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            user = line.split(";")

            _users_.append(
                {
                    "userID": int(user[0]),  # integer
                    "username": str(user[1]),  # string
                    "email": str(user[2]),  # string
                    "password": str(user[3]),  # string
                    "avatar": str(user[4]),  # string
                    "role": str(user[5]),  # string
                    "isBlocked": (user[5]).strip("\n").replace(" ", "")
                    == "True",  # boolean
                }
            )

        file.close()

        return _users_

    def get_categories() -> list:
        """
        Retrieve category data from 'categories.txt' and return a list of category objects.

         Each category object includes:
        - categoryID: Unique identifier for the category (int).
        - category: The name of the category (str).

        :return: List of category objects representing the categories in the database.
        """

        file = open("files/categories.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            category = line.split(";")

            _categories_.append(
                {
                    "categoryID": int(category[0]),  # integer
                    "category": str(category[1]),  # string
                }
            )

        file.close()

        return _categories_

    def get_photos() -> list:
        """
        Retrieve photo data from 'photos.txt' and return a list of photo objects.

        Each photo object includes:
        - photoID: Unique identifier for the photo (int).
        - description: Description of the photo (str).
        - publishedDate: Published date of the photo (str).
        - image: File path or URL for the photo image (str).
        - likes: Number of likes for the photo (int).
        - rating: Rating of the photo (float).
        - categoryID: Category ID of the photo (int).
        - creatorID: Creator ID of the photo (int).

        :return: List of photo objects representing the photos in the database.
        """

        file = open("files/photos.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            photo = line.split(";")

            _photos_.append(
                {
                    "photoID": int(photo[0]),  # integer
                    "description": str(photo[1]),  # string
                    "publishedDate": str(photo[2]),  # string
                    "image": str(photo[3]),  # string
                    "likes": int(photo[4]),  # integer
                    "rating": float(photo[5]),  # float
                    "categoryID": int(photo[6]),  # integer
                    "creatorID": int(photo[7]),  # integer
                }
            )

        file.close()

        return _photos_

    def get_comments() -> list:
        """
        Retrieve comment data from 'comments.txt' and return a list of comment objects.

        Each comment object includes:
        - commentID: Unique identifier for the comment (int).
        - authorID: Author ID of the comment (int).
        - comment: The comment (str).
        - photoID: Photo ID of the comment (int).

        :return: List of comment objects representing the comments in the database.
        """

        file = open("files/comments.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            comment = line.split(";")

            _comments_.append(
                {
                    "commentID": int(comment[0]),  # integer
                    "authorID": int(comment[1]),  # integer
                    "comment": str(comment[2]),  # string
                    "photoID": int(comment[3]),  # integer
                }
            )

        file.close()

        return _comments_

    def create_user(
        username: str,
        email: str,
        password: str,
        avatar: str,
        role: str,
        isBlocked: bool,
    ) -> dict:
        """
        Create a new user and add it to the database.

        Args:
        :param username: User's username (str).
        :param email: User's email address (str).
        :param password: User's password (str).
        :param avatar: File path or URL for user's avatar (str).
        :param role: User's role ('admin', 'regular', 'unsigned') (str).
        :param isBlocked: Indicates if the user is blocked (bool).

        :return: User object representing the new user.
        """

        file = open("files/users.txt", "a", encoding="utf-8")

        # getting the last user id
        last_user = _users_[-1]

        last_user_id = last_user["userID"]

        # increments the last user id
        last_user_id += 1

        # new user dictionary
        new_user = {
            "userID": last_user_id,  # integer
            "username": username,  # string
            "email": email,  # string
            "password": password,  # string
            "avatar": avatar,  # string
            "role": role,  # string
            "isBlocked": isBlocked,  # boolean
        }

        # append the new user to the list
        _users_.append(new_user)

        file.write(
            f"{last_user_id};{username};{email};{password};{avatar};{role};{isBlocked}\n"
        )

        file.close()

        return new_user

    def create_categories(category: str) -> dict:
        """
        Create a new category and add it to the database.

        Args:
        :param category: The name of the category (str).

        :return: Category object representing the new category.
        """

        file = open("files/categories.txt", "a", encoding="utf-8")

        # getting the last category id
        last_category = _categories_[-1]

        last_category_id = last_category["categoryID"]

        # increments the last category id
        last_category_id += 1

        # new category dictionary
        new_category = {
            "categoryID": last_category_id,  # integer
            "category": category,  # string
        }

        # append the new category to the list
        _categories_.append(new_category)

        file.write(f"{last_category_id};{category}\n")

        file.close()

        return new_category

    def create_photos(
        description: str,
        publishedDate: str,
        image: str,
        likes: int,
        rating: float,
        categoryID: int,
        creatorID: int,
    ) -> dict:
        """
        Create a new photo and add it to the database.

        Args:
        :param description: Description of the photo (str).
        :param publishedDate: Published date of the photo (str).
        :param image: File path or URL for the photo image (str).
        :param likes: Number of likes for the photo (int).
        :param rating: Rating of the photo (float).
        :param categoryID: Category ID of the photo (int).
        :param creatorID: Creator ID of the photo (int).

        :return: Photo object representing the new photo.
        """

        file = open("files/photos.txt", "a", encoding="utf-8")

        # getting the last photo id
        last_photo = _photos_[-1]

        last_photo_id = last_photo["photoID"]

        # increments the last photo id
        last_photo_id += 1

        # new photo dictionary
        new_photo = {
            "photoID": last_photo_id,  # integer
            "description": description,  # string
            "publishedDate": publishedDate,  # string
            "image": image,  # string
            "likes": likes,  # integer
            "rating": rating,  # float
            "categoryID": categoryID,  # integer
            "creatorID": creatorID,  # integer
        }

        # append the new photo to the list
        _photos_.append(new_photo)

        file.write(
            f"{last_photo_id};{description};{publishedDate};{image};{likes};{rating};{categoryID};{creatorID}\n"
        )

        file.close()

        return new_photo

    def create_comments(authorID: int, comment: str, photoID: int) -> dict:
        """
        Create a new comment and add it to the database.

        Args:
        :param authorID: Author ID of the comment (int).
        :param comment: The comment (str).
        :param photoID: Photo ID of the comment (int).

        :return: Comment object representing the new comment.
        """

        file = open("files/comments.txt", "a", encoding="utf-8")

        # getting the last comment id
        last_comment = _comments_[-1]

        last_comment_id = last_comment["commentID"]

        # increments the last comment id
        last_comment_id += 1

        # new comment dictionary
        new_comment = {
            "commentID": last_comment_id,  # integer
            "authorID": authorID,  # integer
            "comment": comment,  # string
            "photoID": photoID,  # integer
        }

        # append the new comment to the list
        _comments_.append(new_comment)

        file.write(f"{last_comment_id};{authorID};{comment};{photoID}\n")

        file.close()

        return new_comment

    def update_user(
        userID: int,
        username: str,
        email: str,
        password: str,
        avatar: str,
        role: str,
        isBlocked: bool,
    ) -> dict:
        """
        Updates an existing user in the database with the given data.

        Args:
        :param userID: Unique identifier (int).
        :param username: User's username (str).
        :param email: User's email address (str).
        :param password: User's password (str).
        :param avatar: File path or URL for user's avatar (str).
        :param role: User's role ('admin', 'regular', 'unsigned') (str).
        :param isBlocked: Indicates if the user is blocked (bool).

        :return: User object representing the updated user.
        """

        file = open("files/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/users.txt", "w+", encoding="utf-8")

        for line in lines:
            user = line.split(";")

            if int(user[0]) == userID:
                user[1] = username
                user[2] = email
                user[3] = password
                user[4] = avatar
                user[5] = role
                user[6] = isBlocked

                file.write(
                    f"{user[0]};{user[1]};{user[2]};{user[3]};{user[4]};{user[5]};{user[6]}"
                )
            else:
                file.write(line)

        file.close()

        return {
            "userID": userID,  # integer
            "username": username,  # string
            "email": email,  # string
            "password": password,  # string
            "avatar": avatar,  # string
            "role": role,  # string
            "isBlocked": isBlocked,  # boolean
        }

    def update_photo(
        photoID: int,
        description: str,
        publishedDate: str,
        image: str,
        likes: int,
        rating: float,
        categoryID: int,
        creatorID: int,
    ) -> dict:
        """

        Updates an existing photo in the database with the given data.

        Args:
        :param photoID: Unique identifier for the photo (int).
        :param description: Description of the photo (str).
        :param publishedDate: Published date of the photo (str).
        :param image: File path or URL for the photo image (str).
        :param likes: Number of likes for the photo (int).
        :param rating: Rating of the photo (float).
        :param categoryID: Category ID of the photo (int).
        :param creatorID: Creator ID of the photo (int).
        """

        file = open("files/photos.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/photos.txt", "w+", encoding="utf-8")

        for line in lines:
            photo = line.split(";")

            if int(photo[0]) == photoID:
                photo[1] = description
                photo[2] = publishedDate
                photo[3] = image
                photo[4] = likes
                photo[5] = rating
                photo[6] = categoryID
                photo[7] = creatorID

                file.write(
                    f"{photo[0]};{photo[1]};{photo[2]};{photo[3]};{photo[4]};{photo[5]};{photo[6]};{photo[7]}"
                )
            else:
                file.write(line)

        file.close()

        return {
            photoID: photoID,  # integer
            description: description,  # string
            publishedDate: publishedDate,  # string
            image: image,  # string
            likes: likes,  # integer
            rating: rating,  # float
            categoryID: categoryID,  # integer
            creatorID: creatorID,  # integer
        }

    def delete_category(categoryID: int, category: str) -> None:
        """
        Deletes a category from the database.

        Args:
        :param categoryID: Unique identifier for the category (int).
        :param category: The name of the category (str).

        :return: None
        """

        file = open("files/categories.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/categories.txt", "w+", encoding="utf-8")

        for line in lines:
            category = line.split(";")

            if int(category[0]) != categoryID:
                file.write(line)

        file.close()

    def delete_photo(
        photoID: int,
        description: str,
        publishedDate: str,
        image: str,
        likes: int,
        rating: float,
        categoryID: int,
        creatorID: int,
    ) -> None:
        """
        Deletes a photo from the database.

        Args:
        :param photoID: Unique identifier for the photo (int).
        :param description: Description of the photo (str).
        :param publishedDate: Published date of the photo (str).
        :param image: File path or URL for the photo image (str).
        :param likes: Number of likes for the photo (int).
        :param rating: Rating of the photo (float).
        :param categoryID: Category ID of the photo (int).
        :param creatorID: Creator ID of the photo (int).

        :return: None
        """

        file = open("files/photos.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/photos.txt", "w+", encoding="utf-8")

        for line in lines:
            photo = line.split(";")

            if int(photo[0]) != photoID:
                file.write(line)

        file.close()

    def delete_user(
        userID: int,
        username: str,
        email: str,
        password: str,
        avatar: str,
        role: str,
        isBlocked: bool,
    ) -> None:
        """
        Deletes a user from the database.

        Args:
        :param userID: Unique identifier (int).
        :param username: User's username (str).
        :param email: User's email address (str).
        :param password: User's password (str).
        :param avatar: File path or URL for user's avatar (str).
        :param role: User's role ('admin', 'regular', 'unsigned') (str).
        :param isBlocked: Indicates if the user is blocked (bool).

        :return: None
        """

        file = open("files/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/users.txt", "w+", encoding="utf-8")

        for line in lines:
            user = line.split(";")

            if int(user[0]) != userID:
                file.write(line)

        file.close()

    # initialize the database
    get_users()
    get_categories()
    get_photos()
    get_comments()

    # return the database

    return {
        "users": _users_,
        "categories": _categories_,
        "photos": _photos_,
        "comments": _comments_,
        "create_user": create_user,
        "create_categories": create_categories,
        "create_photos": create_photos,
        "create_comments": create_comments,
        "update_user": update_user,
        "update_photo": update_photo,
        "delete_category": delete_category,
        "delete_photo": delete_photo,
        "delete_user": delete_user,
    }
