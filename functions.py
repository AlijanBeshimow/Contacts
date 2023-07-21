from files import save, load_contacts

from classes import Address, Contact


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


def find_contact():
    contacts = load_contacts()
    user_input = input("Enter contact name to find: ")
    print()
    for contact in contacts:
        if contact.name == user_input:
            print(
                f"{contact.name.capitalize()} - {contact.phone} - {contact.email}  {contact.address}")
            break
    else:
        print("Contact not found. Please check name and try again.")


def update():
    contacts = load_contacts()
    user_input = input("Enter contact name to update: ")
    print()
    for contact in contacts:
        if contact.name == user_input:
            option = input(f"""
What you want to update for contact: {contact.name.capitalize()}

1)Name  
2)Phone  
3)Email  
4)Address

             Choice: """)
            print()
            if option == '1':
                contact.name = input("New name: ")
                print("Name updated")
            if option == '2':
                contact.phone = input("New phone: ")
                print("Phone updated")
            if option == '3':
                contact.email = input("New email: ")
                print("Email updated")
            if option == '4':
                new_address = Address()
                new_address.country = input("Enter country: ")
                new_address.city = input("Enter city: ")
                contact.address = new_address
                print("Address updated")
            save(contacts)
            break
    else:
        print("Contact not found. Please check name and try again.")


def remove_contact():
    contacts = load_contacts()
    user_input = input("Name to remove: ")
    print()
    for contact in contacts:
        if contact.name == user_input:
            contacts.remove(contact)
            save(contacts)
            print("Contact", contact.name.Capitalize(), "Removed")
            break
    else:
        print("Contact not found. Please check name and try again.")


def add_address():
    contacts = load_contacts()
    name = input("Enter contact name: ")
    print()
    for contact in contacts:
        if contact.name == name:
            new_address = Address()
            new_address.country = input("Enter country: ")
            new_address.city = input("Enter city: ")
            contact.address = new_address
            print()
            print("Address Added to", contact.name.capitalize())
            save(contacts)
            break
    else:
        print("Contact not found. Please check name and try again.")
