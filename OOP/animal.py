# Define a class that is a type of Animal (such as Dog or Cat). meaning, your class should not be called Animal, it should be called Dog or Cat or something else creative
#Include 1 class attribute called species
#Include __init__() method
#Include 2 instance attributes
#Include  __str__() method
#Include 1 additional method of your choice
#In another file, instantiate your object.
#Show how you use the __str__() method
#Show how you use the additional method
#Bonus: write another function outside of the class that uses the instance of your object that adds some aspect of functionality
#Include comments! Make your variables and function names self-documenting = name them clearly illustrating what they will do, or what datatype they will hold.
#clarification: "Show how you use the __str__() method" means to simply print an instance of the object. Like we learned - under the hood, print() looks at the str method
class rooster:
    species = "animal"

    def __init__(self, go, feathers):
        self.go = go
        self.feathers = feathers

    def __str__(self):
        return" The rooster will " + self.go

    def eat(self, food):
        print ("My rooster likes to eat " + food)
     