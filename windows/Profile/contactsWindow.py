from tkinter import Label, Listbox, Text, Scrollbar, Toplevel
from styles.colors import colors
from styles.fonts import quickSandBold, quickSandRegular
from models.users import getUserInfo, findUserID
from models.contacts import get_contacts
from utils.profile.profile import insert_contacts


def contactsWindow(email: str):
    """
    This function is used to display the admin contacts of banned users window.

    :param email: str
    """
    # open the window
    _contactsWindow_ = Toplevel()

    userID = findUserID(email)
    userPayload = getUserInfo(userID)

    print(f"contactsWindowPayload: {userPayload}")

    # centering the window
    contactsWindowWidth = 1000  # width of the window
    contactsWindowHeight = 595  # height of the window

    screenWidth = _contactsWindow_.winfo_screenwidth()  # width of the screen

    screenHeight = _contactsWindow_.winfo_screenheight()  # height of the screen

    x = (screenWidth / 2) - (contactsWindowWidth / 2)  # calculate x position

    y = (screenHeight / 2) - (contactsWindowHeight / 2)  # calculate y position

    # setting the window size and position
    # %d = integer
    # %dx%d = width x height
    # %d+%d = x position + y position
    _contactsWindow_.geometry(
        "%dx%d+%d+%d" % (contactsWindowWidth, contactsWindowHeight, x, y)
    )
    _contactsWindow_.title("👤 Profile - Contacts 👥")
    _contactsWindow_.iconbitmap("assets/PhotoShowIcon.ico")
    _contactsWindow_.resizable(0, 0)
    _contactsWindow_.config(bg=colors["primary-50"])

    # ----------------------  Labels ---------------------------
    contactsLabel = Label(
        _contactsWindow_,
        text="Contacts",
        font=quickSandBold(22),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    contactsLabel.place(x=40, y=15)

    listContactsLabel = Label(
        _contactsWindow_,
        text="Select a contact to see more details of the banned user",
        font=quickSandRegular(12),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    listContactsLabel.place(x=40, y=60)
    # ----------------------Contacts List ----------------------
    contacts = get_contacts()

    listUsers = Listbox(
        _contactsWindow_,
        width=20,
        height=10,
        font=quickSandRegular(12),
        bg=colors["secondary-500"],
        fg=colors["primary-50"],
    )

    listUsers.place(x=40, y=100)

    listUsersScrollbar = Scrollbar(
        _contactsWindow_,
        orient="vertical",
        command=listUsers.yview,
        bg=colors["secondary-500"],
        troughcolor=colors["secondary-500"],
    )

    listUsersScrollbar.place(x=242, y=100, height=252)

    listUsers.configure(yscrollcommand=listUsersScrollbar.set)

    insert_contacts(contacts, listUsers)
    # ----------------------  Preview Message ----------------------------
    previewMessageLabel = Label(
        _contactsWindow_,
        text="Preview Message",
        font=quickSandBold(18),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    previewMessageLabel.place(x=550, y=15)

    previewMessageTitle = Label(
        _contactsWindow_,
        text="Title",
        font=quickSandBold(12),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    previewMessageTitle.place(x=550, y=60)

    previewMessageTitle = Label(
        _contactsWindow_,
        text="Message",
        font=quickSandBold(12),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    previewMessageTitle.place(x=550, y=140)

    previewMessage = Text(
        _contactsWindow_,
        width=40,
        height=10,
        font=quickSandRegular(12),
        bg=colors["secondary-400"],
        fg=colors["primary-50"],
    )

    previewMessage.place(x=550, y=180)

    previewTitleContent = Label(
        _contactsWindow_,
        text="",
        font=quickSandRegular(12),
        bg=colors["primary-50"],
        fg=colors["secondary-500"],
    )

    previewTitleContent.place(x=550, y=90)

    previewMessage.configure(state="disabled")

    def preeviewMessageEvent(event):
        """
        This function is used to display the preview message of the selected contact.

        :param event: event
        """

        if len(listUsers.curselection()) == 0:
            previewTitleContent.configure(text="Select a contact to preview the title")
            previewMessage.configure(state="normal")
            previewMessage.delete("1.0", "end")
            previewMessage.insert("end", "Select a contact to preview the message")
            previewMessage.configure(state="disabled")

            return

        # getting the contact selected
        contact = contacts[listUsers.curselection()[0]]

        # inserting the title of the contact in the preview title
        previewTitleContent.configure(text=contact["title"])

        # inserting the message of the contact in the preview message
        previewMessage.configure(state="normal")
        previewMessage.delete("1.0", "end")
        previewMessage.insert("end", contact["message"])
        previewMessage.configure(state="disabled")

    listUsers.bind("<<ListboxSelect>>", preeviewMessageEvent)

    # --------------------- -Events----------------------------

    # event when opening the window
    _contactsWindow_.bind("<FocusIn>", lambda event: preeviewMessageEvent(event))
    _contactsWindow_.grab_set()
