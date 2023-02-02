from person import Person
from datetime import datetime
from allergy import Allergy
 
class Camper(Person):
    def __init__(self, first_name, last_name, date_of_birth):
        self.allergies = []
        self.date_of_birth = datetime.strptime(date_of_birth,"%d/%m/%Y")
        super().__init__(first_name, last_name)  

    def add_allergy(self, allergies: str):
        if Allergy[allergies.upper()] not in self.allergies:
            self.allergies.append(Allergy[allergies.upper()])
        return self.allergies

    def get_age(self):
        camper_age = int(datetime.now().year - self.date_of_birth.year)
        return camper_age

    def __str__(self):
        camper_message = "Camper: " +super().__str__()+ " Age: " + str(self.get_age())
        if self.allergies != []:
            for each in self.allergies:
                camper_message+=" With an allergy of: " + str(each.name)
        return camper_message