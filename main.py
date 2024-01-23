# from windows.Profile.profileWindow import albunsProfileWindow

# if __name__ == "__main__":
#     albunsProfileWindow("pedromst@gmail.com")

from tkinter import Tk, Canvas, Button, NW
from PIL import ImageTk, Image
from styles.colors import *
from styles.fonts import *
from windows.Authentication.loginWindow import loginWindow
from utils.widgets.button import on_enter, on_leave


class main:
    # attributes

    window: Tk = None
    canvas: Canvas = None
    mainImage: ImageTk.PhotoImage = None
    logoImage: ImageTk.PhotoImage = None
    sloganText: Canvas.create_text = None
    signInButton: Button = None

    def __init__(
        self,
        window: Tk = None,
        canvas: Canvas = None,
        mainImage: ImageTk.PhotoImage = None,
        logoImage: ImageTk.PhotoImage = None,
        sloganText: Canvas.create_text = None,
        signInButton: Button = None,
    ) -> None:
        """
        This class is used to display the main window.
        :param window: Tk
        :param canvas: Canvas
        :param mainImage: ImageTk.PhotoImage
        :param logoImage: ImageTk.PhotoImage
        :param sloganText: Canvas.create_text
        :param signInButton: Button

        :return: None

        """

        self.window = window
        self.canvas = canvas
        self.mainImage = mainImage
        self.logoImage = logoImage
        self.sloganText = sloganText
        self.signInButton = signInButton

        # methods

    def _main_(self):
        """
        This method is used to create the main window.

        """

        self.window = Tk()
        self.window.title("PhotoShow")
        self.window.geometry("1350x700")

        # to insert the icon on the window
        self.window.iconbitmap("assets/PhotoShowIcon.ico")

        # remove the maximize button
        self.window.resizable(0, 0)

        # canvas
        self.canvas = Canvas(self.window, width=1350, height=700)
        self.canvas.place(x=0, y=0)

        self.mainImage = Image.open("assets/images/main_background.png")
        self.mainImage = self.mainImage.resize((1350, 700))

        self.mainImage = ImageTk.PhotoImage(self.mainImage)

        self.canvas.create_image(0, 0, image=self.mainImage, anchor=NW)

        self.logoImage = Image.open("assets/images/Logo.png")

        self.logoImage = self.logoImage.resize((600, 200))

        self.logoImage = ImageTk.PhotoImage(self.logoImage)

        self.canvas.create_image(390, 50, image=self.logoImage, anchor=NW)

        self.sloganText = self.canvas.create_text(
            550,
            300,
            text="Every Pixel Tells a Tale",
            font=(quickSandBold(25)),
            fill=colors["accent-500"],
            anchor=NW,
        )

        self.signInButton = Button(
            width=18,
            height=2,
            text="Sign In",
            master=self.canvas,
            borderwidth=10,
            font=quickSandBold(16),
            background=colors["accent-300"],
            bd=0,
            highlightthickness=0,
            activebackground=colors["accent-100"],
            cursor="hand2",
        )

        self.signInButton.place(x=600, y=500)
        self.signInButton.bind("<Button-1>", lambda event: loginWindow(self.window))
        self.signInButton.bind("<Enter>", lambda e: on_enter(e, self.signInButton))
        self.signInButton.bind("<Leave>", lambda e: on_leave(e, self.signInButton))

        self.window.mainloop()


if __name__ == "__main__":
    main()._main_()
