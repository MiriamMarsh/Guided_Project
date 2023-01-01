import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv("hotel_bookings.csv")

def catplot(graph):
    print("This is my catplot chart for" ,graph) 

def create_catplot(x, graph):
    sns.catplot(x=x, kind='count', data=df).set(title = 'Bar chart of {} column'.format(x))
    catplot(graph)
    return create_catplot

def titlename(b):
    print(datetime.now())
    print("Miriam Marsh")
    return titlename

def imports(a, b):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    from datetime import datetime
    import sys
    titlename(b)
    print("This is a new project for", a)
    return imports

def create_boxenplot(y):
    sns.boxenplot(x= df[y])
    return