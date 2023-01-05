class ShabbosMaker:
    time = 'time'
    hand = 'hand'
    taste = "shabbos__taam"
    def __init__(self, experience, good_spirit):   
        self.experience = experience
        self.good_spirit = good_spirit

    def cook_food(self, utensil, food, heating_source):
        print("I'm cooking the " + food +  "using a " + utensil + "on the " + heating_source)

    def clean_house(self, equipment,area, detergent):
        print("I'm cleaning with the " + equipment  + "the " + area + "with " + detergent)

    def set_table(self,table_cloth, utensils, paper_goods):
        print("I'm setting the table with " + table_cloth + "and putting out the " + utensils + "and " + paper_goods)   

def main():
    mommy = ShabbosMaker("1","2")
    mommy.cook_food("cholent ", "crockpot ", "counter ")
    mommy.clean_house("sponga stick " , "dinning room ", "Sano ")
    mommy.set_table("white table cloth ", "forks ", "plates ")
main()    


# It should have at least 1 class variable, at least 1 instance variable,  at least 3 methods, and at least 1 method that takes in a parameter besides self..
# Create an instance of your ShabbosMaker and use it! (i.e. cause it to make Shabbos by calling your functions)
# Don’t forget that as a best practive, your outermost layer of code should be in a function called main()