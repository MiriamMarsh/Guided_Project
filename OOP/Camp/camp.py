from bunk import Bunk
from counsler import Counsler
from person import Person
from camper import Camper
from allergys import Allergy
class Camp:
    def __init__(self,name, max_bunks) -> None:
        self.name = name
        self.max_bunks = max_bunks
        self.num_bunks = 0
        self.bunks = []
        self.person = []
        self.allergy = []

    def add_counsler(self,firstname, lastname, hire_date, salary):
        self.person.append(Counsler(firstname,lastname, hire_date,salary))

    def add_camper(self, firstname, lastname, dob):
        self.person.append(Camper(firstname, lastname, dob))

    def add_allergy(self, allergy):
        #all_allergies = [member.name for member in Allergy]
        self.allergy.append (Allergy[allergy.upper()])   

        #self.firstname = firstname
        #self.lastname = lastname
   # def add_bunk(self, bunk_name, counsler, firstname, lastname):
   #self.bunks.append(Bunk(bunk_name,counsler, firstname ,lastname))

    def add_bunk(self, bunk_name, counsler, firstname, lastname):
        self.person.append(Bunk(firstname,lastname,bunk_name, counsler))
       # counsler = self.add_bunk(firstname,lastname,bunk_name, counsler)

        # if counsler ==None:
        #     raise Exception ("counsler not found with that name")
        # else:
        #     if self.num_bunks < self.max_bunks:
        #         newbunk = Bunk(bunk_name,counsler)
        #         self.bunks.append(newbunk)  
        #         self.num_bunks += 1
        #     else:
        #         raise Exception ("you have reached the maximum number of bunks")          

    def find_camper(self,firstname,lastname):
        for camper in self.camper:
            for person in self.person:
                if isinstance(person, camper) and person.firstname == firstname and person.lastname ==lastname:
                    return person
                return None 


    def find_bunk(self, bunk_name) :
        
        for bunk in self.bunks:
            if bunk.bunk_name == bunk_name:
                return bunk
        return None                   

    def find_counsler(self,firstname,lastname):
        for person in self.person:
            if isinstance(person,Counsler) and person.firstname == firstname and person.lastname ==lastname:
                return person
            return None   


    def __str__(self) -> str:
        s = "Welcome to camp "+ self.camp_name +"\nOur bunks:\n"
        for b in  self.bunks:
            s+=str(b)
        s+= "\nIn our camp \n" + str(self.num_bunks)+" bunks.\nWe don't allow more than "+str(self.max_bunks)+" bunks."
        for p in self.persons:
            s+="\n*"
            s+=str(p)
        s+="\nare happy to part of our camp."
        return s