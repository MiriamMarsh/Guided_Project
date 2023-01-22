#Go through the code and identify which variables will belong to the Person class and 
# which variables will belong to the Store class. For example, last name is a variable that will belong to the Person class.
#Write a Person class with instance attributes for those variables. For example, 
# take last name and make it an attribute of the person class. Find 2 more variables that should belong to the 
# Person class and make them attributes. You do not need to pass these attributes as parameters into the constructor. 
# However, you must assign the attribute to some value inside the constructor.
#Now do that with all the variables that should belong in the Store class.
#Don’t forget to make the attributes private and make getters and setters for every attribute.
#Now make a file called main_shopping_assignment.py. Copy the shoppingassigment.py into that file. 
# Now updated that file to use the objects that you defined.  
#In other words, instantiate a Person. Set each of the Person attributes to the value they should be set to. 
# For example, if your instance of Person is a variable called person, set person’s last_name attribute to whatever 
# the user entered for last_name (hint: use a setter). Do this for all the attributes of your 2 objects.


class Person:
    def __init__ (self,last_name, address, method):
        self.__last_name = last_name
        self.__address = address
        self.__pref_transport_method = method

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def pref_transport_method(self):
        return self.__pref_transport_method