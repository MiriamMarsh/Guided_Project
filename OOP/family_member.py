#from parent_member import Parent
#from child_member import Child

class FamilyMember():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def babysit(self):
        return ("Please be on time!")

    def __str__(self):
        return "My Name is : " + self.firstname + self.lastname + ". My age is: "+ str(self.__age)

    # def main():
    #     parent1 = Parent("Miriam", "Marsh", 20)
    #     print(parent1.firstname + parent1.lastname + parent1.age)

    #     child1 = Child  ("Miriam", "Marsh", 1)
    #     print(child1.firstname)
    #     print(child1.lastname + child1.age)
    #     print(child1.babysit())   

    # if __name__ == "__main__":
    #     main()
#Override the babysit() method. Return a string that describes what babysitting constitutes for any Family_Member (
# hint- use super()) PLUS any additional description that pertains when a child is carrying out the babysitting.

