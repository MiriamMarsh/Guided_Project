import pandas as pd
from datetime import datetime
import sys
name=sys.argv[1]
teacher=sys.argv[2]
 #   def welcome_to_class(name):
 #   print("welcome to this class", name)
 #   print(datetime.now())

# welcome_to_class(name)
import datetime
def classes(name, teacher):
    d=datetime.datetime.now()
    print("Welcome to this class,", name)
    print(d)
    time=d.strftime("%H:%M")
    while True:
        if time < ("09:00"):
            print("before class")
        elif time > ("09:00") and  time < ("10:50"):
             print("during class")
        elif time > ("10:50") and time < ("11:10"):
             print("break time")  
        elif time > ("11:10") and time < ("13:00"):
             print("Class Time")
        else:
            print("Make sure to do your HMWK!")    
        if teacher == "Mrs.A":
            print ("We will be learning the letter A")
        if teacher == "Mrs.B":
            print ("We will be learning the letter B Today with,", teacher)
        break
classes(name, teacher) 

    # "before class" if its before 9:00, "during class" if its during class time, and "break" if its 10:50-11:10
   
   