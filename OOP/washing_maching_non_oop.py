def set_settings (color, temp, speed, cycle, ): #color options are whites, lights, and darks 
    print("my temperature is" + str(temp))
    print("my spin speed is" + str(speed))
    print("my cycle type is" + cycle)

def soak(door_is_locked):
    if door_is_locked==True:
        print("I'm soaking!")
    else:
        print("Close Door") 


def agitate(detergent):
    print("scrubbing with" + detergent)    


def rinse():
    print("rinsing")   

def wash_laundry(temp,speed,cycle, door_is_locked, detergent):
    set_settings(temp,speed,cycle)   
    soak(door_is_locked)
    agitate(detergent)
    rinse()

wash_laundry(30, 1000,"cottons", True, "Persil")    