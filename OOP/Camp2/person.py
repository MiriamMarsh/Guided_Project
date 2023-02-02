class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Person):
            result = self.first_name == other.first_name and self.last_name == other.last_name
            return result
        else:
            return False

    def __str__(self):
        message = self.first_name +" "+ self.last_name
        return message 