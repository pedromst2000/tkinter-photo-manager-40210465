import re as regex
from styles.fonts import quickSandRegularUnderline, quickSandRegular

isPasswordVisible = False


def checkEmail(email: str) -> bool:
    """
     this function will check if the email is valid with regex
     Regex explanation:
     [^@]+ - matches any character except @ one or more times
     @ - matches @ literally
     [^@]+ - matches any character except @ one or more times
     \. - matches . literally
     [^@]+ - matches any character except @ one or more times

    :param email: str

    :return: bool

    """

    if not regex.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False  # if dont match the pattern, return False

    return True  # if match the pattern, return True


def checkUsername(username: str) -> bool:
    """
    this function will check if the username is valid with regex
    Regex explanation:
    ^ - matches the beginning of the string
    [a-zA-Z0-9_.-] - matches any character in the list one or more times
    $ - matches the end of the string

    :param username: str

    :return: bool

    """

    if not regex.match(r"^[a-zA-Z0-9_.-]+$", username):
        return False  # if dont match the pattern, return False

    if regex.match(r"^[0-9]+$", username):
        return False 

    return True  # if match the pattern, return True


def hidePasswordIcon(
    ImageTk: object,
    Image: object,
    canvasManagePassword: object,
    NW: object,
    X: int,
    Y: int,
) -> None:
    """
    this function will display the hide password icon

    :param ImageTk: object
    :param Image: object
    :param canvasManagePassword: object
    :param NW: object
    :param X: int
    :param Y: int

    :return: None

    """

    eye = Image.open("assets/images/UI_Icons/Hide_Eye_Icon.png")

    eye = eye.resize((60, 40))

    canvasManagePassword.image = ImageTk.PhotoImage(eye)

    canvasManagePassword.create_image(0, 0, anchor=NW, image=canvasManagePassword.image)

    canvasManagePassword.place(x=X, y=Y)


def showPasswordIcon(
    ImageTk: object,
    Image: object,
    canvasManagePassword: object,
    NW: object,
    X: int,
    Y: int,
) -> None:
    """
    this function will display the show password icon

    :param ImageTk: object
    :param Image: object
    :param canvasManagePassword: object
    :param NW: object
    :param X: int
    :param Y: int

    :return: None

    """

    eye = Image.open("assets/images/UI_Icons/Eye_Icon.png")

    eye = eye.resize((60, 40))

    canvasManagePassword.image = ImageTk.PhotoImage(eye)

    canvasManagePassword.create_image(0, 0, anchor=NW, image=canvasManagePassword.image)

    canvasManagePassword.place(x=X, y=Y)


def togglePasswordVisibility(
    ImageTk: object,
    Image: object,
    canvasManagePassword: object,
    NW: object,
    inputPassword: object,
    X: int,
    Y: int,
) -> None:
    """
    this function will toggle the password visibility and change the icon as well

    :param ImageTk: object
    :param Image: object
    :param canvasManagePassword: object
    :param NW: object
    :param inputPassword: object
    :param X: int
    :param Y: int

    :return: None

    """

    global isPasswordVisible

    if isPasswordVisible == False:  # if the password is not visible
        inputPassword.config(show="")  # show the password
        isPasswordVisible = True  # change the variable to True
        showPasswordIcon(
            # X and Y are the coordinates of the canvas
            ImageTk,
            Image,
            canvasManagePassword,
            NW,
            X,
            Y,
        )
    else:
        inputPassword.config(show="*")
        isPasswordVisible = False
        hidePasswordIcon(ImageTk, Image, canvasManagePassword, NW, X, Y)


def manageVisibility(
    ImageTk: object,
    Image: object,
    canvasManagePassword: object,
    NW,
    inputPassword: object,
    X: int,
    Y: int,
) -> None:
    """
    this function will manage the visibility of the password

    :param ImageTk: object
    :param Image: object
    :param canvasManagePassword: object
    :param NW: object
    :param inputPassword: object
    :param X: int
    :param Y: int

    :return: None

    """

    global isPasswordVisible

    if inputPassword.get() != "":  # if the password input is not empty
        if isPasswordVisible == False:  # and if the password is not visible
            hidePasswordIcon(  # will display the hide password icon
                ImageTk, Image, canvasManagePassword, NW, X, Y
            )
        if isPasswordVisible == True:  # and if the password is visible
            showPasswordIcon(  # will display the show password icon
                ImageTk, Image, canvasManagePassword, NW, X, Y
            )
    else:
        # if the password input is empty, the canvas will be hidden and not showing any icon (either hide or show password icon)
        canvasManagePassword.place_forget()

    # on mouse hover in and out underline the text


def on_enter(e: object, label: object) -> None:
    """
    this function will underline the text when the mouse is on the label

    :param e: object
    :param labelInfo: object

    :return: None
    """

    label.config(font=quickSandRegularUnderline(12))


def on_leave(e: object, label: object) -> None:
    """
    this function will remove the underline of the text when the mouse is not on the label

    :param e: object
    :param labelInfo: object

    :return: None
    """

    label.config(font=quickSandRegular(12))
