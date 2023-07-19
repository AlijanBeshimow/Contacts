from files import save, load_contacts

from classes import Contact


def add():
    contacts = load_contacts()
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    new_contact = Contact(name=name, phone=phone, email=email)
    contacts.append(new_contact)
    save(contacts)
    print()
    print("New contact added")


def view():
    contacts = load_contacts()
    print(*contacts)


def find():
    contacts = load_contacts()
    found_contact = False
    user_input = input("Name to find: ").capitalize()
    print()
    for contact in contacts:
        if contact.name == user_input:
            print(contact.name, contact.phone, contact.email)
        found_contact = True
    if not found_contact:
        print("Contact not found")


def update():
    contacts = load_contacts()
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
    contacts = load_contacts()
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
        print("Contact not found")
