class Database:
    users = []
    categories = []
    photos = []
    comments = []
    albuns = []
    favorites = []

    # constructor
    def __init__(
        self,
        users: list = [],
        categories: list = [],
        photos: list = [],
        comments: list = [],
        albuns: list = [],
        favorites: list = [],
    ):
        """
        Initialize the database.

        :param users: List of user objects representing the users in the database.
        :param categories: List of category objects representing the categories in the database.
        :param photos: List of photo objects representing the photos in the database.
        :param comments: List of comment objects representing the comments in the database.
        :param albuns: List of album objects representing the albums in the database.
        :param favorites: List of favorite objects representing the favorites in the database.
        """

        self.users = users
        self.categories = categories
        self.photos = photos
        self.comments = comments
        self.albuns = albuns
        self.favorites = favorites

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
        - followers: user's followers (int).
        - isBlocked: Indicates if the user is blocked (bool).

        :return: List of user objects representing the users in the database.
        """
        file = open("files/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            user = line.split(";")

            # ignoring the first line
            if user[0] == "userID":
                continue

            self.users.append(
                {
                    "userID": int(user[0]),  # integer
                    "username": user[1],  # string
                    "email": user[2],  # string
                    "password": user[3],  # string
                    "avatar": user[4],  # string
                    "role": user[5],  # string
                    "followers": int(user[6]),  # integer
                    "isBlocked": user[7].strip("\n").replace(" ", "")
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

            # ignoring the first line
            if category[0] == "categoryID":
                continue

            self.categories.append(
                {
                    "categoryID": int(category[0]),  # integer
                    "category": category[0].strip("\n"),
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
        - views: Number of views for the photo (int).
        - rating: Rating of the photo (float).
        - categoryID: Category ID of the photo (int).
        - creatorID: Creator ID of the photo (int).
        - albumID: Album ID of the photo each belongs to (int).

        :return: List of photo objects representing the photos in the database.
        """
        file = open("files/photos.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            photo = line.split(";")

            # ignoring the first line
            if photo[0] == "photoID":
                continue

            self.photos.append(
                {
                    "photoID": int(photo[0]),  # integer
                    "description": photo[1],  # string
                    "publishedDate": photo[2],  # string
                    "image": photo[3],  # string
                    "likes": int(photo[4]),  # integer
                    "views": int(photo[5]),  # integer
                    "rating": photo[5],  # float
                    "categoryID": photo[6],  # integer
                    "creatorID": photo[7],  # integer
                    "albumID": photo[8].strip("\n"),  # integer
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

            # ignoring the first line
            if comment[0] == "commentID":
                continue

            self.comments.append(
                {
                    "commentID": int(comment[0]),  # integer
                    "authorID": comment[1],  # integer
                    "comment": comment[2],  # string
                    "photoID": comment[3].strip("\n"),  # integer
                }
            )

        file.close()

        return self.comments

    def get_albuns(self) -> list:
        """
        Retrieve album data from 'albuns.txt' and return a list of album objects.

        Each album object includes:
        - albumID: Unique identifier for the album (int).
        - name: Name of the album (str).
        - creatorID: Creator ID of the album (int).

        :return: List of album objects representing the albums in the database.
        """

        file = open("files/albuns.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            album = line.split(";")

            # ignoring the first line
            if album[0] == "albumID":
                continue

            self.albuns.append(
                {
                    "albumID": int(album[0]),  # integer
                    "name": album[1],  # string
                    "creatorID": album[2].strip("\n"),  # integer
                }
            )

        file.close()

        return self.albuns

    def get_favorites(self) -> list:
        """
        Retrieve favorite data from 'favorites.txt' and return a list of favorite objects.

        Each favorite object includes:
        - albumID: Unique identifier for the album (int).
        - userID: User ID of the user (int).

        :return: List of favorite objects representing the favorites in the database.
        """

        file = open("files/favorites.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            favorite = line.split(";")

            # ignoring the first line
            if favorite[0] == "albumID":
                continue

            self.favorites.append(
                {
                    "albumID": int(favorite[0]),  # integer
                    "userID": favorite[1].strip("\n"),  # integer
                }
            )

            file.close()

            return self.favorites

    def create_user(self, user: dict) -> None:  # add a new user to the database
        """
        Create a new user and add it to the database.

        :param user: Dictionary containing the user data.

        :return: Dictionary containing the user data.

        """

        # add a new user to the database
        file = open("files/users.txt", "a", encoding="utf-8")

        users = self.get_users()

        # getting the last user id
        last_user_id = users[-1]["userID"]

        # incrementing the last user id
        last_user_id += 1

        # new user dictionary
        new_user = {
            "userID": last_user_id,
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "avatar": user.avatar,
            "role": user.role,
            "followers": user.followers,
            "isBlocked": user.isBlocked,
        }

        # appending the new user to the users list
        self.users.append(new_user)

        file.write(
            f"\n{new_user['userID']};{new_user['username']};{new_user['email']};{new_user['password']};{new_user['avatar']};{new_user['role']};{new_user['followers']};{new_user['isBlocked']}"
        )
        file.close()

    def create_category(
        self, category: dict
    ) -> None:  # add a new category to the database
        """
        Create a new category and add it to the database.

        :param category: Dictionary containing the category data.

        :return: Dictionary containing the category data.

        """

        file = open("files/categories.txt", "a", encoding="utf-8")

        categories = self.get_categories()

        # getting the last category id
        last_category_id = categories[-1]["categoryID"]

        # incrementing the last category id
        last_category_id += 1

        # new category dictionary
        new_category = {
            "categoryID": last_category_id,
            "category": category.category,
        }

        # appending the new category to the categories list
        self.categories.append(new_category)

        file.write(f"\n{new_category['categoryID']};{new_category['category']}")

        file.close()

    def create_photo(self, photo: dict) -> None:  # add a new photo to the database
        """
        Create a new photo and add it to the database.

        :param photo: Dictionary containing the photo data.

        :return: Dictionary containing the photo data.

        """

        file = open("files/photos.txt", "a", encoding="utf-8")

        photos = self.get_photos()

        # getting the last photo id
        last_photo_id = photos[-1]["photoID"]

        # incrementing the last photo id
        last_photo_id += 1

        # new photo dictionary
        new_photo = {
            "photoID": last_photo_id,
            "description": photo.description,
            "publishedDate": photo.publishedDate,
            "image": photo.image,
            "likes": photo.likes,
            "views": photo.views,
            "rating": photo.rating,
            "categoryID": photo.categoryID,
            "creatorID": photo.creatorID,
        }

        # appending the new photo to the photos list
        self.photos.append(new_photo)

        file.write(
            f"{new_photo['photoID']};{new_photo['description']};{new_photo['publishedDate']};{new_photo['image']};{new_photo['likes']};{new_photo['views']};{new_photo['rating']};{new_photo['categoryID']};{new_photo['creatorID']}\n"
        )

        file.close()

    def create_comment(
        self, comment: dict
    ) -> None:  # add a new comment to the database
        """
        Create a new comment and add it to the database.

        :param comment: Dictionary containing the comment data.

        :return: Dictionary containing the comment data.

        """

        file = open("files/comments.txt", "r", encoding="utf-8")

        comments = self.get_comments()

        # getting the last comment id
        last_comment_id = comments[-1]["commentID"]

        # incrementing the last comment id
        last_comment_id += 1

        # new comment dictionary
        new_comment = {
            "commentID": last_comment_id,
            "authorID": comment.authorID,
            "comment": comment.comment,
            "photoID": comment.photoID,
        }

        self.comments.append(new_comment)

        file.write(
            f"{new_comment['commentID']};{new_comment['authorID']};{new_comment['comment']};{new_comment['photoID']}\n"
        )

        file.close()

    def create_album(self, album: dict) -> None:  # add a new album to the database
        """
        Create a new album and add it to the database.

        :param album: Dictionary containing the album data.

        :return: Dictionary containing the album data.

        """

        file = open("files/albuns.txt", "a", encoding="utf-8")

        albuns = self.get_albuns()

        # getting the last album id
        last_album_id = albuns[-1]["albumID"]

        # incrementing the last album id
        last_album_id += 1

        # new album dictionary

        new_album = {
            "albumID": last_album_id,
            "name": album.name,
            "creatorID": album.creatorID,
        }

        self.albuns.append(new_album)

        file.write(
            f"{new_album['albumID']};{new_album['name']};{new_album['creatorID']}\n"
        )

        file.close()

    def create_favorite(
        self, favorite: dict
    ) -> None:  # add a new favorite album to the database
        """
        Create a new favorite album and add it to the database.

        :param favorite: Dictionary containing the favorite album data.

        :return: Dictionary containing the favorite album data.

        """

        file = open("files/favorites.txt", "a", encoding="utf-8")

        favorites = self.get_favorites()

        # getting the last favorite id
        last_favorite_id = favorites[-1]["albumID"]

        # incrementing the last favorite id
        last_favorite_id += 1

        # new favorite dictionary
        new_favorite = {
            "albumID": last_favorite_id,
            "userID": favorite.userID,
        }

        self.favorites.append(new_favorite)

        file.write(f"{new_favorite['albumID']};{new_favorite['userID']}\n")

        file.close()

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

    def update_album(self, album: dict) -> None:  # update a album in the database
        """
        Update a album in the database.

        :param album: Dictionary containing the album data.

        :return: Dictionary containing the album data.
        """

        file = open("files/albuns.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/albuns.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != album.albumID:
                file.write(line)

            else:
                file.write(line)

        file.close()

        return album

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
    
    def delete_favorite(self, favorite: dict) -> None:
        """
        Delete a favorite album from the database.

        :param favorite: Dictionary containing the favorite album data.

        :return: Dictionary containing the favorite data.

        """

        file = open("files/favorites.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("files/favorites.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != favorite.albumID:
                file.write(line)

            else:
                file.write(line)

        file.close()
