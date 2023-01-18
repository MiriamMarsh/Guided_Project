from parent_member import Parent
from child_member import Child
    
def main():
    parent1 = Parent("Miriam ", " Marsh ", 20)

    print("Mommy:" + parent1.firstname + parent1.lastname + str(parent1.age))

    child1 = Child  ("Baby ", " Marsh ", 1)
    print("Baby: " + child1.firstname + child1.lastname + str(child1.age))
    # print(child1.lastname)
    # print (str(child1.age))
    print(child1.babysit())   

if __name__ == "__main__":
    main()
#Override the babysit() method. Return a string that describes what babysitting constitutes for any Family_Member (
# hint- use super()) PLUS any additional description that pertains when a child is carrying out the babysitting.