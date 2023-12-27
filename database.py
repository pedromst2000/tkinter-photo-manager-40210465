class Database:
    users = []
    categories = []
    photos = []
    comments = []

    # constructor
    def __init__(
        self,
        users: list = [],
        categories: list = [],
        photos: list = [],
        comments: list = [],
    ):
        """
        Initialize the database.

        :param users: List of user objects representing the users in the database.
        :param categories: List of category objects representing the categories in the database.
        :param photos: List of photo objects representing the photos in the database.
        :param comments: List of comment objects representing the comments in the database.
        """

        self.users = users
        self.categories = categories
        self.photos = photos
        self.comments = comments

    # methods
    def get_users(self) -> list:
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
            self.users.append(
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

        return self.users

    def get_categories(self) -> list:
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
            self.categories.append(
                {
                    "categoryID": int(category[0]),  # integer
                    "category": str(category[0]).strip("\n"),
                }
            )

        file.close()

        return self.categories

    def get_photos(self) -> list:
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
            self.photos.append(
                {
                    "photoID": int(photo[0]),  # integer
                    "description": str(photo[1]),  # string
                    "publishedDate": str(photo[2]),  # string
                    "image": str(photo[3]),  # string
                    "likes": int(photo[4]),  # integer
                    "rating": float(photo[5]),  # float
                    "categoryID": int(photo[6]),  # integer
                    "creatorID": int(photo[7].strip("\n")),  # integer
                }
            )

        file.close()

        return self.photos

    def get_comments(self) -> list:
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
            self.comments.append(
                {
                    "commentID": int(comment[0]),  # integer
                    "authorID": int(comment[1]),  # integer
                    "comment": str(comment[2]),  # string
                    "photoID": int(comment[3].strip("\n")),  # integer
                }
            )

        file.close()

        return self.comments

    def create_user(self, user: dict) -> None:  # add a new user to the database
        """
        Create a new user and add it to the database.

        :param user: Dictionary containing the user data.

        :return: Dictionary containing the user data.

        """

        # add a new user to the database
        file = open("files/users.txt", "a", encoding="utf-8")

        # getting the last user id
        last_user_id = self.users[-1]["userID"]

        # incrementing the last user id
        last_user_id += 1

        # new user dictionary
        new_user = {
            "userID": last_user_id,
            "username": user["username"],
            "email": user["email"],
            "password": user["password"],
            "avatar": user["avatar"],
            "role": user["role"],
            "isBlocked": user["isBlocked"],
        }

        # appending the new user to the users list
        self.users.append(new_user)

        file.write(
            f"{new_user['userID']};{new_user['username']};{new_user['email']};{new_user['password']};{new_user['avatar']};{new_user['role']};{new_user['isBlocked']}\n"
        )

        file.close()

        return new_user

    def create_category(
        self, category: dict
    ) -> None:  # add a new category to the database
        """
        Create a new category and add it to the database.

        :param category: Dictionary containing the category data.

        :return: Dictionary containing the category data.

        """

        file = open("files/categories.txt", "a", encoding="utf-8")

        # getting the last category id
        last_category_id = self.categories[-1]["categoryID"]

        # incrementing the last category id
        last_category_id += 1

        # new category dictionary
        new_category = {
            "categoryID": last_category_id,
            "category": category["category"],
        }

        # appending the new category to the categories list
        self.categories.append(new_category)

        file.write(f"{new_category['categoryID']};{new_category['category']}\n")

        file.close()

        return new_category

    def create_photo(self, photo: dict) -> None:  # add a new photo to the database
        """
        Create a new photo and add it to the database.

        :param photo: Dictionary containing the photo data.

        :return: Dictionary containing the photo data.

        """

        file = open("files/photos.txt", "a", encoding="utf-8")

        # getting the last photo id
        last_photo_id = self.photos[-1]["photoID"]

        # incrementing the last photo id
        last_photo_id += 1

        # new photo dictionary
        new_photo = {
            "photoID": last_photo_id,
            "description": photo["description"],
            "publishedDate": photo["publishedDate"],
            "image": photo["image"],
            "likes": photo["likes"],
            "rating": photo["rating"],
            "categoryID": photo["categoryID"],
            "creatorID": photo["creatorID"],
        }

        # appending the new photo to the photos list
        self.photos.append(new_photo)

        file.write(
            f"{new_photo['photoID']};{new_photo['description']};{new_photo['publishedDate']};{new_photo['image']};{new_photo['likes']};{new_photo['rating']};{new_photo['categoryID']};{new_photo['creatorID']}\n"
        )

        file.close()

        return new_photo

    def create_comment(
        self, comment: dict
    ) -> None:  # add a new comment to the database
        """
        Create a new comment and add it to the database.

        :param comment: Dictionary containing the comment data.

        :return: Dictionary containing the comment data.

        """

        file = open("files/comments.txt", "r", encoding="utf-8")

        # getting the last comment id
        last_comment_id = self.comments[-1]["commentID"]

        # incrementing the last comment id
        last_comment_id += 1

        # new comment dictionary
        new_comment = {
            "commentID": last_comment_id,
            "authorID": comment["authorID"],
            "comment": comment["comment"],
            "photoID": comment["photoID"],
        }

        self.comments.append(new_comment)

        file.write(
            f"{new_comment['commentID']};{new_comment['authorID']};{new_comment['comment']};{new_comment['photoID']}\n"
        )

        file.close()

        return new_comment

    def update_user(self, user: dict) -> None:  # update a user in the database
        """
        Update a user in the database.

        :param user: Dictionary containing the user data.

        :return: Dictionary containing the user data.

        """

        file = open("files/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/users.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != user.userID:
                file.write(line)

            else:
                file.write(line)

        file.close()

        return user

    def update_photo(self, photo: dict) -> None:  # update a photo in the database
        """
        Update a photo in the database.

        :param photo: Dictionary containing the photo data.

        :return: Dictionary containing the photo data.

        """

        file = open("files/photos.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/photos.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != photo.photoID:
                file.write(line)

            else:
                file.write(line)

        file.close()

        return photo

    def delete_category(
        self, category: dict
    ) -> None:  # delete a category from the database
        """
        Delete a category from the database.

        :param category: Dictionary containing the category data.

        :return: Dictionary containing the category data.
        """

        file = open("files/categories.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/categories.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != category.categoryID:
                file.write(line)

            else:
                file.write(line)

        file.close()

    def delete_photo(self, photo: dict) -> None:  # delete a photo from the database
        """
        Delete a photo from the database.

        :param photo: Dictionary containing the photo data.

        :return: Dictionary containing the photo data.

        """

        file = open("files/photos.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/photos.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != photo.photoID:
                file.write(line)

            else:
                file.write(line)

        file.close()

    def delete_user(self, user: dict) -> None:
        """
        Delete a user from the database.

        :param user: Dictionary containing the user data.

        :return: Dictionary containing the user data.

        """

        file = open("files/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/users.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != user.userID:
                file.write(line)

            else:
                file.write(line)

        file.close()
