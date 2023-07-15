import pickle

from classes import Contact


def setup():
    try:
        with open("contacts.pickle", 'rb') as file:
            pickle.load(file)
    except:
        with open("contacts.pickle", 'wb') as file:
            pickle.dump([], file)


def save(list_to_save):
    with open("contacts.pickle", 'wb') as file:
        pickle.dump(list_to_save, file)


def load():
    with open("contacts.pickle", 'rb') as file:
        loaded_contact = pickle.load(file)
    return loaded_contact


def add():
    contacts = load()
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    new_contact = Contact(name=name, phone=phone, email=email)
    contacts.append(new_contact)
    save(contacts)
    print()
    print("New contact added")


def find():
    contacts = load()
    found_contact = False
    user_input = input("Name to find: ").capitalize()
    print()
    for contact in contacts:
        if contact.name == user_input:
            print(contact.name, contact.phone)
        found_contact = True
    if not found_contact:
        print("Contact not found")


def update():
    contacts = load()
    found_contact = False
    user_input = input("Name to update: ")
    print()
    for contact in contacts:
        if contact.name == user_input:
            contact.name = input("New name: ")
            contact.phone = input("New phone: ")
            contact.email = input("New email: ")
            found_contact = True
            save(contacts)
            print()
            print("Contact updated")
    if not found_contact:
        print("Contact not found")


def remove_contact():
    contacts = load()
    removed = False
    user_input = input("Name to remove: ")
    print()
    for contact in contacts:
        if contact.name == user_input:
            contacts.remove(contact)
            save(contacts)
            removed = True
            print(contact.name, "Removed")
    if not removed:
        print("COntact not found")
