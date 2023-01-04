import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
#from analysis_functions import *
#from plotting_functions import *
#from mainapp import *

df = pd.read_csv("hotel_bookings.csv")

# describe and analyze dataframe
# what will the function do: 
    # print value counts for all columns
    # find_val_counts(df) - this is the function for df written below
    # print info , head and describe in the analyze function below.


def titlename(col_name):
    print(datetime.now())
    print("Miriam Marsh")
    print("This is a new project for", col_name)

#This function errored on the last line so I didn't use it.
# The function which  gives valuecounts for all cols which takes in the df.
def find_val():
    for col in df.columns:
        print(col.value_counts().sort_index)
        
#Analyzing Data in many different ways for the dataframe.
def analyze():
    print(df.head()), print(df.describe()), print(df.info()), print(df.columns)



