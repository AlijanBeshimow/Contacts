class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"""
{self.name}-{self.phone}-{self.email}""".replace("'", '').replace(",", '').replace("(", '').replace(")", '')
