from functions import add, find, load_contacts, update, remove_contact, delete_all, view


load_contacts()

while True:
    option = input("""
[A]dd
[V]iew
[F]ind
[U]pdate
[R]emove
[D]elete All
[Q]uit
                Choice: """)
    print()
    if option == "a":
        add()
    if option == "v":
        view()
    if option == "f":
        find()
    if option == "u":
        update()
    if option == "r":
        remove_contact()
    if option == "d":
        delete_all()
    if option == "q":
        break
