from classes.Contact import Contact
from classes.User import User


def get_contacts() -> list:
    """
    Function to get all contacts

    :return: list
    """
    contacts = Contact().get_contacts()
    
    if contacts == None:
        return []

    return [
        {
            "contactID": contact["contactID"],
            "title": contact["title"],
            "message": contact["message"],
            "username": User().get_user(contact["userID"])["username"],
        }
        for contact in contacts
    ]
