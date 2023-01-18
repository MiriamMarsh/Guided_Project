from family_member import FamilyMember

class Child(FamilyMember):
    def __init__(self,firstname,lastname,age):
        super().__init__(firstname, lastname, age)

    def babysit(self):
        return super().babysit() + "I'll try to behave myself. Pleas take good care of me."    
