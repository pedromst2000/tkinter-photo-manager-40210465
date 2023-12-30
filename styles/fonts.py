import tkinter.font as tkFont


def quickSandRegular(size: int) -> tkFont:
    """
    This function is used to set the font family to QuickSand Regular.

    :param size: The size of the font.

    :return: The font.
    """

    return tkFont.Font(family="QuickSand", size=size, weight="normal")


def quickSandBold(size: int) -> tkFont:
    """
    This function is used to set the font family to QuickSand Bold.

    :param size: The size of the font.

    :return: The font.
    """

    return tkFont.Font(family="QuickSand", size=size, weight="bold")


def quickSandRegularUnderline(size: int) -> tkFont:
    """
    This function is used to set the font family to QuickSand Regular Underline.

    :param size: The size of the font.

    :return: The font.
    """

    return tkFont.Font(family="QuickSand", size=size, weight="normal", underline=1)


def quickSandBoldUnderline(size: int) -> tkFont:
    """
    This function is used to set the font family to QuickSand Bold Underline.

    :param size: The size of the font.

    :return: The font.
    """

    return tkFont.Font(family="QuickSand", size=size, weight="bold", underline=1)
