# Write an abstract Employee class and 2 concrete classes for HourlyEmployee and Salariedemployee
# Employee constructor should accept 2 parameters: firstname and lastname. Assign them to attributes
# Employee should define a concrete property for full_name.
# Employee should define an abstract method for get salary
# HourlyEmployee should accept 2 parameters in addition to the parameters that it needs for the base class. 
# The 2 additional parameters are hourly_rate and hours_worked_this_week. Assign them to attributes.
# HourlyEmployee should define a concrete version of the get_salary method which will calculate the salary based 
# on hourly_rate and hours_worked_this_week
# Salaried_Employee’s constructor should accept 1 parameter in addition to the 2 required for the base class. 
# The additional parameter is weekly_salary. Assign it to an attribute.
# SalariedEmployee should define a concrete version of get_salary() using the weekly_salary attribute.
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, fname, lname):
        super().__init__()
        self.fname = fname
        self.lname = lname

    @abstractmethod
    def get_salary(self):
        pass

    @property
    def fullname(self):
        return self.fname + " " + self.lname

class Hourly(Employee):
    def __init__(self, fname, lname, hourly_rate , hours_worked_this_week):
        super().__init__(fname,lname)
        self.hourly_rate = hourly_rate
        self.hours_worked_this_week = hours_worked_this_week

    
    # def fullname(self):
    #     return self.fullname(Employee)

    def get_salary(self):
        return self.hourly_rate * self.hours_worked_this_week


class Salary(Employee):
    def __init__(self, fname,lname,weekly_salary):
        super().__init__(fname,lname)
        self.weekly_salary = weekly_salary

    def get_salary(self):
        return self.weekly_salary

def main():
    employee1 = Hourly("Miriam", "marsh", 1000, 4 )
    employee2 = Salary("Chevy", "stern" , "5000")
    employee3=  Salary("chilled", "bitachon", "100")
    employee4 = Salary ("Tzip", "marsh", "200")
    employee5 = Hourly ("Miri", "marshmello", 1001, 4 )
    Employees_list = [employee1,employee2,employee3, employee4, employee5]
    for employee in Employees_list:
        print("Employee Name: " + str(employee.fullname)+ " " +  " Weekly salary: " + str(employee.get_salary()))

main()        


