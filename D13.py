## Day 13 Challenge ##

# Provided

import pandas as pd
df = pd.read_csv('aus_weather.csv')
df = df[df["Location"] == "Melbourne"]
df.head()

# Work

#plots were not being drawn so had to use basic functions to estimate

#Using a histogram, what is the most likely temperature at 9am (Temp9am) in Melbourne?
df['Temp9am'].median()
df['Temp9am'].mode()

#Using a boxplot, does it ever rain (using variable Rainfall) in Melbourne? If yes, what was the highest daily amount recorded?
df['Rainfall'].max() #essentially gives answer since only one option has max rainfall over 80mm