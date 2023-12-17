from tkinter import Entry
from styles.fonts import *
from styles.colors import *


# inputText = Entry(
#     width=30,
#     borderwidth=0,
#     font=quickSandRegular(14),
#     background=colors["primary-50"],
#     fg=colors["secondary-500"],
#     highlightthickness=0,
#     cursor="hand2",
# )


def _Input_(
    width: int,
    borderwidth: int,
    fontSize: str,
    placeX: int,
    placeY: int,
) -> None:
    """
    This function is used to create a input and to be resuable along the interface was a widget.

    parameters:

    width: int
    borderwidth: int
    fontSize: int
    placeX: int
    placeY: int

    """

    _Input_ = Entry(
        width=width,
        borderwidth=borderwidth,
        font=quickSandBold(fontSize),
        background=colors["secondary-300"],
        fg=colors["secondary-500"],
        highlightthickness=0,
        cursor="xterm",
    )

    _Input_.place(x=placeX, y=placeY)

    # on focus in event changing the background color and the foreground color
    # background color = secondary-500 foreground color = primary- 50

    def on_focus_in(e):
        _Input_["background"] = colors["secondary-500"]
        _Input_["fg"] = colors["primary-50"]

    def on_focus_out(e):
        _Input_["background"] = colors["secondary-300"]
        _Input_["fg"] = colors["secondary-500"]

    _Input_.bind("<FocusIn>", on_focus_in)

    _Input_.bind("<FocusOut>", on_focus_out)
