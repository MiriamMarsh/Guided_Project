import pandas as pd
from datetime import datetime
import sys
name = sys.argv[1]
def welcome_to_class(name):
    print("welcome to this class", name)
    print(datetime.now())

welcome_to_class(name)
   