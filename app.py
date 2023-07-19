from functions import add, find, update, remove_contact, view


while True:
    option = input("""
1. Add Contact
2. View All Contacts
3. Find Contact
4. Update Contact
5. Remove Contact

                   
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

    if option == "q":
        break
