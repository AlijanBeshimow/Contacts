class Contact:
    def __init__(self, name="", phone="", email="", address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"""
{self.name.capitalize()} - {self.phone} - {self.email}  {self.address}"""


class Address(Contact):
    def __init__(self):
        super().__init__()
        self.country = ""
        self.city = ""

    def __str__(self):
        return f"{self.country.capitalize()} {self.city.capitalize()}"
