import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hotel_bookings.csv")

def create_catplot(x):
    sns.catplot(x=x, kind='count', data=df).set(title = 'Bar chart of {} column'.format(x))
    return

def create_boxenplot(y):
    sns.boxenplot(x= df[y])
    return

