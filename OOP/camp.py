from bunk import Bunk
from counsler import Counsler
from person import Person
from camper import Camper
class Camp:
    def __init__(self,name, max_bunks) -> None:
        self.name = name
        self.max_bunks = max_bunks
        self.num_bunks = 0
        self.bunks = []
        self.people = []

    def add_counsler(self,firstname, lastname, hire_date, salary):
        self.people.append(Counsler(firstname,lastname,hire_date,salary))

    def add_camper(self, firstname, lastname, dob):
        self.people.append(Camper(firstname, lastname, dob))

    def add_bunk(self, bunk_name, counsler, firstname, lastname):
        self.bunks.append(Bunk(bunk_name,counsler, firstname ,lastname))

    def place_camper():


        


        