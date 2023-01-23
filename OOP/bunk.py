from counsler import Counsler
from person import Person
from camper import Camper

class Bunk:
    def __init__(self, bunkname, counsler, firstname, lastname) -> None:
        self.bunkname = bunkname
        self.counsler = counsler
        self.firstname - firstname
        self.lastname = lastname
        self.campers = []

    def add_camper(self, camper):
        self.campers.append(camper)

    def __str__(self) -> str:
        return str(self.counsler) + " is the counsler of bunk " + self.bunkname   
