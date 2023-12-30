from styles.colors import *

# on hover effect changing the background color
def on_enter(e: object, button: object) -> None:
    """
    This function will change the background color of the button when the mouse is on it.

    :param e: object
    :param button: object

    :return: None
    """

    button["background"] = colors["accent-100"]


def on_leave(e: object, button: object) -> None:
    """
    This function will change the background color of the button when the mouse is not on it.

    :param e: object
    :param button: object

    :return: None
    """

    button["background"] = colors["accent-300"]
