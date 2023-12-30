from styles.colors import *


# Global variable
last_focused_input = None


def on_focus_in(e: object, input: object) -> None:
    """
    This function will change the background color and the foreground color of the input when the input is focused.

    :param e: object
    :param input: object

    :return: None
    """

    input["background"] = colors["secondary-500"]
    input["fg"] = colors["primary-50"]
    input.config(insertbackground=colors["primary-50"])


def on_focus_out(e: object, input: object) -> None:
    """
    This function will change the background color and the foreground color of the input when the input is not focused.

    :param e: object
    :param input: object

    :return: None
    """

    input["background"] = colors["secondary-300"]
    input["fg"] = colors["secondary-500"]
    input.config(insertbackground=colors["secondary-500"])


def on_click_outside(e: object, window: object, *input_fields: object) -> None:
    """
    This function will change the background color and the foreground color of the input when the input is not focused.

    :param e: object
    :param window: object
    :param input_fields: object

    :return: None
    """

    global last_focused_input
    for input_field in input_fields:
        if input_field.winfo_containing(e.x_root, e.y_root) == input_field:
            last_focused_input = input_field
            return
    window.focus_set()
