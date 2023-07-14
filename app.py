from functions import setup, add, load, find, update


setup()


while True:
    option = input("""
[A]dd
[V]iew
[F]ind
[U]pdate
[Q]uit
                Choice: """)
    print()
    if option == "a":
        add()
    if option == "v":
        print(*load())
    if option == "f":
        find()
    if option == "u":
        update()
    if option == "q":
        break
