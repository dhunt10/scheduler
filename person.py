class person:
    name = []
    email = []
    phone = []
    club = []

    def __init__(self, name, email=None, phone=None, club=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.club = club
