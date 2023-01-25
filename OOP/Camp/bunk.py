from counsler import Counsler
from person import Person
from camper import Camper

class Bunk:
    def __init__(self, bunk_name, counsler,firstname,lastname) -> None:
        self.bunk_name = bunk_name
        self.counsler = counsler
        self.firstname = firstname
        self.lastname = lastname
        self.campers = []

    def add_camper(self, camper):
        self.campers.append(camper)

    def __str__(self) -> str:
        return str(self.counsler) + " is the counsler of bunk " + self.bunkname  + str(self.campers) 
