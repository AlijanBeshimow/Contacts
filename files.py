import pickle


def load_contacts():
    try:
        with open("contacts.pickle", 'rb') as file:
            contacts = pickle.load(file)
            return contacts
    except:
        with open("contacts.pickle", 'wb') as file:
            pickle.dump([], file)
            return []


def save(list_to_save):
    with open("contacts.pickle", 'wb') as file:
        pickle.dump(list_to_save, file)
