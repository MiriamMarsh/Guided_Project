from person import Person
from datetime import datetime
class Counselor(Person):
    def __init__(self, first_name, last_name, hire_date: str, salary):
        self.hire_date = datetime.strptime(hire_date, "%d/%m/%y")
        self.salary = salary
        super().__init__(first_name, last_name)
    def __str__(self) -> str:
        counselor_message = "Counselor: " + super().__str__()+  " hired on: {} with a salary of {}".format(str(self.hire_date), str(self.salary))
        return counselor_message