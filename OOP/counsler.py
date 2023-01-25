from person import Person
class Counsler(Person):
    def __init__(self,firstname, lastname):
        super().__init__(firstname, lastname)

    def __str__(self) -> str:
        
        