from allergys import Allergy
from person import Person
import pandas as pd
import time
import datetime

class Camper(Person):
    def __init__(self, firstname, lastname, dob) -> None:
        super().__init__(firstname, lastname)
        self.allergy = []
        self.dob = datetime.strptime(dob,"%Y-%m-%d")
    



    def get_age(self, dob):
        self.pd.to_datetime(dob = dob)
        self.age=datetime.DateTime.now-dob
        return int(datetime.now().year - self.dob.year)
        
    #def __str__(self):
    # s = super.(__str__()) self.get_age()
    # return s       
# camper1 = Camper("Miriam", 'Marsh', 1/1/2011)    
# camper1.add_allergy('eggs')
# print(camper1.add_allergy)
