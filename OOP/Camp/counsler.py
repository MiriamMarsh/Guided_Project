from person import Person
import decimal
from datetime import datetime
class Counsler(Person):
    def __init__(self,firstname, lastname, date_hired:str, salary: decimal):
        super().__init__(firstname, lastname)
        self.hire_date = datetime.strptime(date_hired, "%Y-%m-%d")
        self.salary = salary

    def __str__(self) -> str:
       return super().__str__ + "cousler higer date " + str(self.hire_date)+ "salary: " + decimal(self.salary)
    