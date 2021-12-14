import csv
import pandas as pd
import matplotlib.pyplot as pltt

DATA_INPUT = "filtered_data.csv"

df = pd.read_csv(DATA_INPUT)

# Modifying date
df['date'] = df['date'].map(lambda date: date.split('/')[0] +'/'+ date.split('/')[1]+'/' + '20' + date.split('/')[-1])

# Removing spaces from str start and end 
df['start'] = df['start'].map(lambda start: start.replace(' ', ''))
df['end'] = df['end'].map(lambda end: end.replace(' ', ''))

# Casting str prices as floating points
df['start'] = df['start'].map(lambda start: float(start))
df['end'] = df['end'].map(lambda end: float(end))

# Formating/parsing date 
df['date']=pd.to_datetime(df['date'],format='%d/%m/%Y')

# Adding augmentation number
df['aug']= 100.00/df['start']*(df['end']-df['start'])

print(df)
########  Ploting data using seaborn 
# Import necessary packages
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Use white grid plot background from seaborn
sns.set(font_scale=0.5, style="whitegrid")


#######################

sns.pairplot(data=df, hue='tribunal')

# Create figure and plot space
fig, ax = plt.subplots(figsize=(100, 100))

# Add x-axis and y-axis
ax.scatter(df['date'],
        df['aug'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="aug percent",
       title="market temperature")

plt.setp(ax.get_xticklabels(), rotation=45)
plt.show()

