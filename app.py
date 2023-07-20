from files import remove_all_contact
from functions import add, add_address, find, update, remove_contact, view


while True:
    option = input("""
1. Add Contact
2. View All Contacts
3. Find Contact
4. Update Contact Details
5. Remove Contact
6. Add Address to Contact
7. Remove All Contacts

                   
                           Choice: """)
    print()
    if option == "1":
        add()
    if option == "2":
        view()
    if option == "3":
        find()
    if option == "4":
        update()
    if option == "5":
        remove_contact()
    if option == '6':
        add_address()
    if option == '7':
        remove_all_contact()
    if option == "q":
        break
