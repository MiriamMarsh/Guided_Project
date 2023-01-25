from camp import Camp
from camper import Camper
1
def main():
    our_camp = Camp("Camp Integralytic", 40)

    menu_choice = None
    while menu_choice != 0:
        menu_choice = get_menu_choice()
        if menu_choice == 1: #add counselor
            firstname =input ("Please type your first name: ")
            lastname = input ("Please type your last name: ")
            hire_date = input ("what is your hire date? %Y-%m-%d ")
            salary = input ("Please enter your salary for payment ")
            print("Counselor Was Added Successfully! Thank You! ")
            our_camp.add_counsler(firstname,lastname, hire_date, salary)
            
        elif menu_choice == 2: #add bunk
            
            firstname =input ("Please type your first name: ")
            lastname = input ("Please type your last name: ")
            bunk_name = input ("What's your bunk name? ")
            counsler = input ("What's your counslers name? ")
            our_camp.add_bunk(firstname,lastname, bunk_name, counsler)
            print("Bunk Was Added Successfully! Thank You! ")

        elif menu_choice == 3: #add camper
            our_camp.add_camper(firstname,lastname, dob)
            firstname =input ("Please type your first name: ")
            lastname = input ("Please type your last name: ")
            dob = input("Please type your DOB(Y,M,D): ")
        elif menu_choice == 4: #add an allergy
            our_camp.add_allergy(firstname,lastname, allergy)
            firstname =input ("Please type your first name: ")
            lastname = input ("Please type your last name: ")
            allergy = input ("Please enter your allergies: ")
            print(counsler)
        elif menu_choice == 5: #assign camper to bunk
            our_camp.find_bunk(firstname,lastname,bunk_name)
            firstname =input ("Please type your first name: ")
            lastname = input ("Please type your last name: ")
            bunk_name = input ("What your bunk name? ")
        elif menu_choice == 6: # exit
           print("You've exited the program! I hope you enjoyed and will come back NEXT YEAR!!")
                
def get_menu_choice():
    menu = "\n1. Add A Counselor"
    menu +=	"\n2. Add a Bunk" 
    menu +=	"\n3. Add a Camper" 
    menu +=	"\n4. Add an Allergy"
    menu +=	"\n5. Assign a Camper to a Bunk"
    menu +=	"\n6. Display Camp data"
    menu +=	"\n0. Exit Application"

    choice = input(menu + "\nPlease enter 1-6 (or 0 to exit): ")
    return int(choice)

if __name__ == "__main__":
    main()
