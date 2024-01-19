from tkinter import ttk
import tkinter as tk


def insert_users(users: list, usersTable: ttk.Treeview):
    """
    This function is used to insert the users into the table.

    :param users: list
    :param usersTable: ttk.Treeview

    """

    for user in users:
        usersTable.insert(
            "",
            "end",
            values=(
                user["username"],
                user["email"],
                user["role"],
                "Blocked" if user["isBlocked"] else "Not Blocked",
            ),
        )


def insert_categories(categories: list, categoriesList: tk.Listbox):
    """
    This function is used to insert the categories into the table.

    :param categories: list
    :param categoriesList: tk.Listbox

    """

    for category in categories:
        categoriesList.insert("end", category)


def filteringUsersList(
    filterUsernameInput: ttk.Entry,
    filterEmailInput: ttk.Entry,
    usersTable: ttk.Treeview,
    filter_users: callable,
    checkEmail: callable,
    messagebox: tk.messagebox,
    manageWindow: tk.Tk,
):
    """
    This function is used to filter the users by username or email or both.

    :param filterUsernameInput: ttk.Entry
    :param filterEmailInput: ttk.Entry
    :param usersTable: ttk.Treeview
    :param filter_users: callable
    :param checkEmail: callable

    """

    # get the username and email
    username = filterUsernameInput.get()
    email = filterEmailInput.get()

    # check if the email is valid
    if email != "" and not checkEmail(email):
        messagebox.showerror(
            "Error", "Please enter a valid email.", parent=manageWindow
        )
        return

    # filter the users
    users = filter_users(username, email)

    # clear the table
    usersTable.delete(*usersTable.get_children())

    # insert the users into the table
    insert_users(users, usersTable)

    # clear the inputs
    filterUsernameInput.delete(0, "end")
    filterEmailInput.delete(0, "end")


def changingRole(
    usersTable: ttk.Treeview,
    initialRoleVal: ttk.Combobox,
    change_role: callable,
    get_users_list: callable,
    messagebox: tk.messagebox,
    manageWindow: tk.Tk,
):
    """
    This function is used to change the role of the user.

    :param usersTable: ttk.Treeview
    :param initialRoleVal: ttk.Combobox
    :param change_role: callable
    :param get_users_list: callable
    :param messagebox: tk.messagebox
    :param manageWindow: tk.Tk
    """

    # check if the user is selected
    if not usersTable.selection():
        messagebox.showerror("Error", "Please select a user.", parent=manageWindow)
        return

    # if there is any user selected but the role is not selected
    if initialRoleVal.get() == "select role" and usersTable.selection():
        messagebox.showerror("Error", "Please select a role.", parent=manageWindow)
        return

    username = usersTable.item(usersTable.selection())["values"][0]
    newRole = initialRoleVal.get()

    # check if the role is already the same
    if newRole == usersTable.item(usersTable.selection())["values"][2]:
        messagebox.showerror(
            "Error", f'"{username}" is already {newRole}.', parent=manageWindow
        )
        return

    messagebox.showinfo(
        "Success",
        f'The role of "{username}" was changed successfully',
        parent=manageWindow,
    )

    change_role(username, newRole)

    users = get_users_list()

    # clearing the table
    usersTable.delete(*usersTable.get_children())

    # insert the users into the table
    for user in users:
        usersTable.insert(
            "",
            "end",
            values=(
                user["username"],
                user["email"],
                user["role"],
                "Blocked" if user["isBlocked"] else "Not Blocked",
            ),
        )


def changingStatus(
    usersTable: ttk.Treeview,
    initialStatusVal: ttk.Combobox,
    block_user: callable,
    unblock_user: callable,
    get_users_list: callable,
    messagebox: tk.messagebox,
    manageWindow: tk.Tk,
):
    """
    This function is used to change the status of the user.

    :param usersTable: ttk.Treeview
    :param initialStatusVal: ttk.Combobox
    :param block_user: callable
    :param unblock_user: callable
    :param get_users_list: callable
    :param messagebox: tk.messagebox
    :param manageWindow: tk.Tk
    """

    if not usersTable.selection():
        messagebox.showerror("Error", "Please select a user.", parent=manageWindow)
        return

    if initialStatusVal.get() == "select status" and usersTable.selection():
        messagebox.showerror("Error", "Please select a status.", parent=manageWindow)
        return

    username = usersTable.item(usersTable.selection())["values"][0]
    newStatus = initialStatusVal.get()

    # check if is already blocked or unblocked
    if (
        newStatus == "blocked"
        and usersTable.item(usersTable.selection())["values"][3] == "Blocked"
    ):
        messagebox.showerror(
            "Error", f'"{username}" is already blocked.', parent=manageWindow
        )
        return

    elif (
        newStatus == "unblocked"
        and usersTable.item(usersTable.selection())["values"][3] == "Not Blocked"
    ):
        messagebox.showerror(
            "Error", f'"{username}" is already unblocked.', parent=manageWindow
        )
        return

    if newStatus == "blocked":
        messagebox.showinfo(
            "Success", f'"{username}" was blocked successfully.', parent=manageWindow
        )

    elif newStatus == "unblocked":
        messagebox.showinfo(
            "Success", f'"{username}" was unblocked successfully.', parent=manageWindow
        )
    if newStatus == "blocked":
        block_user(username)
    elif newStatus == "unblocked":
        unblock_user(username)
    users = get_users_list()

    # # clear the table
    usersTable.delete(*usersTable.get_children())

    # # insert the users into the table
    for user in users:
        usersTable.insert(
            "",
            "end",
            values=(
                user["username"],
                user["email"],
                user["role"],
                "Blocked" if user["isBlocked"] else "Not Blocked",
            ),
        )


def addCategory(
    categoryInput: ttk.Entry,
    categoriesList: tk.Listbox,
    add_category: callable,
    messagebox: tk.messagebox,
    manageWindow: tk.Tk,
):
    """
    This function is used to add a new category.

    :param categoryInput: ttk.Entry
    :param categoriesList: tk.Listbox
    :param add_category: callable
    :param messagebox: tk.messagebox
    :param manageWindow: tk.Tk
    """
    category = categoryInput.get()

    if category != "":
        # if the category was added successfully
        if add_category(category):
            messagebox.showinfo(
                "Success", "The category was added successfully!", parent=manageWindow
            )
            categoriesList.insert("end", category)
            categoryInput.delete(0, "end")

        else:
            messagebox.showerror(
                "Error",
                "The category already exists, please try again!",
                parent=manageWindow,
            )

    else:
        messagebox.showerror("Error", "Please enter a category!", parent=manageWindow)


def deleteCategory(
    categoriesList: tk.Listbox,
    delete_category: callable,
    messagebox: tk.messagebox,
    manageWindow: tk.Tk,
):
    """
    This function is used to delete a category.

    :param categoriesList: tk.Listbox
    :param delete_category: callable
    :param messagebox: tk.messagebox
    :param manageWindow: tk.Tk

    """

    if categoriesList.curselection() == ():
        messagebox.showwarning(
            "Warning", "Please select a category to delete", parent=manageWindow
        )
        return

    # get the selected category
    selectedCategory = categoriesList.get(categoriesList.curselection())

    # ask the user if he is sure to delete the category
    confirm = messagebox.askyesno(
        "Confirm",
        f"Are you sure you want to delete {selectedCategory}?",
        parent=manageWindow,
    )

    if confirm == True:
        messagebox.showinfo(
            "Success",
            f"{selectedCategory} was deleted successfully",
            parent=manageWindow,
        )
        # delete the category
        delete_category(selectedCategory)

        # delete the selected category from the listbox
        categoriesList.delete(categoriesList.curselection())

    else:
        return
