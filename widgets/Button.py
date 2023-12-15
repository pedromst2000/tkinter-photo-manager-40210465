from tkinter import Button
from styles.fonts import *
from styles.colors import *


def _Button_(
    width: str,
    height: str,
    text: str,
    fontSize: str,
    window: object,
    placeX: int,
    placeY: int,
):
    """

    This function is used to create a button and to be resuable along the interface was a widget.

    parameters:

    width: str
    height: str
    text: str
    fontSize: str
    window: object
    placeX: int
    placeY: int

    """

    _Button_ = Button(
        window,
        text=text,
        width=width,
        height=height,
        borderwidth=10,
        font=quickSandBold(fontSize),
        background=colors["accent-300"],
        bd=0,
        highlightthickness=0,
        activebackground=colors["accent-100"],
        cursor="hand2",
    )
    _Button_.place(x=placeX, y=placeY)

    # on hover effect changing the background color
    def on_enter(e):
        _Button_["background"] = colors["accent-100"]

    def on_leave(e):
        _Button_["background"] = colors["accent-300"]

    _Button_.bind("<Enter>", on_enter)
    _Button_.bind("<Leave>", on_leave)
