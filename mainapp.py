#Connecting all the functions from the py script files with abbreviations for function name calling
import analysis_functions as af
import plotting_functions as pf

#Importing all the correct imports needed for this GP.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

#This reads in the csv file of hotel_bookings for our project.
df = pd.read_csv("hotel_bookings.csv")

#The titlename function will output my name, the title of the file and a breif description of the project
af.titlename("Python Script Functions for Seaborn Guided Project")
#The anaylze function will output for me some of the very important anayzing functions for my project. Including info, describe, and head)
af.analyze()
#The Value Count function will print out the value counts with sort index combined.
#af.find_val()
#This out_plot function will output a catplot chart with a title name, description of the chart as well as save the chart image with the 
#correct chart name.
pf.create_catplot("children")
#This catplot function will output a catplot chart with a title name, description of the chart as well as save the chart image with the 
#correct chart name.
pf.create_catplot("adults")
#This Boxenplot function will output a Boxenplot chart with a title name, description of the chart as well as save the chart image with the 
#correct chart name.
pf.create_boxenplot("stays_in_weekend_nights")

