from camper import Camper
from counselor import Counselor

class Bunk:

    def __init__(self, bunk_name: str, counselor: Counselor):
        self.bunk_name = bunk_name
        self.counselor = counselor
        self.campers = []
    def add_camper(self, camper: Camper):
        if camper not in self.campers:
            self.campers.append(camper)
        return self.campers
    def __str__(self) -> str:
        bunk_message = "\nBunk Name: {}\n{}.".format(self.bunk_name, str(self.counselor))
        for each in self.campers:
            bunk_message+="\n"
            bunk_message+=str(each)
        return bunk_message