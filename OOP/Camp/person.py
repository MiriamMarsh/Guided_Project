

class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return 'Hello ' + self.firstname + " "  + self.lastname + " Welcome to CAMP!!"



