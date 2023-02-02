from camp import Camp
import logging
import traceback 
def main():

    our_camp = Camp("Camp Integralytic", 20)
    menu_choice = None
    while menu_choice != 0:
        menu_choice = get_menu_choice()
        try:
            if menu_choice == 1:
                fname = input("Enter first name of counselor:")
                lname = input("Enter last name of counselor:")
                hire_date = input("Enter the date counselor was hired in dd/mm/yy format:")
                salary = input("Enter starting salary:")
                try:
                    our_camp.add_counselor(fname, lname, hire_date, salary) 
                except ValueError as exc:
                    print(str(exc))
                    logging.error(str(exc) + traceback.format_exc())
                    hire_date = input("Hire date was wrong format, please re-enter in this format: dd/mm/yy")
                    our_camp.add_counselor(fname, lname, hire_date, salary)
                    print("New counselor added")

            elif menu_choice == 2: #add bunk
                bunk_name = input("Enter the name of the bunk:")
                counselor_fname = input("Enter the first name of the counselor:")
                counselor_lname = input("Enter the last name of the counselor:")
                our_camp.add_bunk(bunk_name, counselor_fname, counselor_lname) 
            
            elif menu_choice == 3: #add camper
                fname = input("Enter first name of camper:")
                lname = input("Enter last name of camper:")
                dob = input("Enter date of birth in dd/mm/yyyy format")
                our_camp.add_camper(fname, lname, dob)
                
            elif menu_choice == 4: #add an allergy
                fname = input("Enter the first name of the camper with an allergy:")
                lname = input("Enter the last name of the camper with an allergy")
                allergies = input("Enter the food allergy:")
                our_camp.add_allergy(fname, lname, allergies) 

            elif menu_choice == 5: #assign camper to bunk
                fname = input("Enter the first name of the camper:")
                lname = input("Enter the last name of the camper:")
                bunk_name = input("Enter the name of the bunk where the camper should be placed:")
                our_camp.place_camper(fname, lname, bunk_name)     

            elif menu_choice == 6: #
                print(our_camp) 

            elif menu_choice == 0:
                print("You have exited the application.")    
                break
            #print("Task completed")
            logging.info("choice: " + str(menu_choice)+"completed Successfully")      
        except  Exception as ex:
            print("ERROR!" + str(ex))
            logging.error(str(ex) + traceback.format_exc())
    return None

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

