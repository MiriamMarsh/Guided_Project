#from analysis_functions import *
#from plotting_functions import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv("hotel_bookings.csv")

#Plotting bar chart from a column
#ars: df, col
#plot, and output to folder - save the plot
#plotting scatter plot from two columns
#args: df, col1, and col2
#plot, output to folder

#All my markdowns for the functions are on the mainapp.py file
def catplot(x):
    print("This is my catplot chart for",x) 
    return
def create_catplot(col):
    sns.catplot(x=col, kind='count', data=df)
    catplot(col)
    title = plt.title('Bar chart of {} column'.format(col))
    plt.savefig('{}.png'.format(title)) 
    plt.clf()
    return
def create_boxenplot(col):
    sns.boxenplot(x= df[col])
    title = plt.title('Bar chart of {} column'.format(col))
    plt.savefig('{}.png'.format(title))  
    plt.clf()
    return
