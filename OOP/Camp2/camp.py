from person import Person
from counselor import Counselor
from camper import Camper
from bunk import Bunk
import logging
import os
import sys
import an_filled as an

logging.basicConfig(filename= an.LOG_FILE,
                    filemode='a+',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


class Camp:
    def __init__(self, camp_name: str, max_bunks: int):
        self.camp_name = camp_name
        self.max_bunks = max_bunks
        self.bunks = []
        self.num_bunks = 0
        self.persons = []
# In camp.py, raise an exception in the following cases:
# Add_counselor, add_camper: if a counselor/camper with that name already exists
# Add_bunk: if the counselor with that name is not found, if the max number of bunks is exceeded
# Place_camper: if the bunk with that name was not found, if the camper with that name was not found
# Bonus: Instead of simply raise Exception(“message”), raise a specific type of exception that matches the scenario. S
# See the table in this link for the built in python exception types: https://www.tutorialsteacher.com/python/error-types-in-python


    def find_counselor(self, fname, lname):
        for person in self.persons:
            if isinstance(person, Counselor):
                if person.first_name == fname and person.last_name == lname:
                    return person
        return None

    def find_camper(self, fname, lname):
        for person in self.persons:
            if isinstance(person, Camper):
                if person.first_name == fname and person.last_name == lname:
                    return person
        return None
    def find_bunk(self, bunk_name: Bunk):
        for bunk in self.bunks:
            if bunk.bunk_name == bunk_name:
                return bunk
        

    def add_counselor(self, fname, lname, hire_date, salary):
        c = self.find_counselor(fname, lname)
        if c == None:
            self.persons.append(Counselor(fname, lname, hire_date, salary))
        else:
            raise Exception("Counselor already exists")

    def add_camper(self, fname, lname, dob):
        ca = self.find_camper(fname, lname)
        if ca == None:
            self.persons.append(Camper(fname, lname, dob))
        else:
            raise Exception("Camper already exists")
    
    def add_bunk(self, bunk_name, counselor_fname, counselor_lname):
        my_counselor = self.find_counselor(counselor_fname, counselor_lname)
        if my_counselor == None:
            raise Exception ("Counselor was not found")
        else:
            if self.max_bunks > self.num_bunks:
                self.bunks.append(Bunk(bunk_name, my_counselor))
                self.num_bunks+=1
            else:
                raise Exception("You have reached the max number of bunks allowed.")

    def place_camper(self, fname, lname, bunk_name):
        bunk = self.find_bunk(bunk_name)
        if bunk == None:
            raise Exception("could not find bunk")
        my_camper = self.find_camper(fname, lname)
        if my_camper == None:
            raise Exception("could not find camper")
        else:
            bunk.add_camper(my_camper)

    def add_allergy(self, fname, lname, allergies: str):
        my_camper = self.find_camper(fname, lname)
        my_camper.add_allergy(allergies)

    def __str__(self):
        description= "Welcome to {}! There are {} bunks.".format(self.camp_name, self.num_bunks)
        for each in self.bunks:
            description+=str(each)
        return description

        
# def main():
#     my_camp = Camp("camp fun", 5)
#     my_camp.add_counselor("Rivky", "Stern", "02/05/22", "500")
#     my_camp.add_bunk("Juniors", "Rivky", "Stern")
#     my_camp.add_camper("Leah", "Friedman", '01/01/2000')
#     my_camp.add_camper("Sara", "Berg", "06/07/2000")
#     my_camp.add_allergy("Leah", "Friedman", "milk")
#     my_camp.place_camper("Leah", "Friedman", "Juniors")
#     my_camp.place_camper("Sara", "Berg", "Juniors")
#     print(my_camp)

# main()
