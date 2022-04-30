### Day 20 Challenge ###

## Provided ##

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
conn = sqlite3.connect("world.db")

## Work ##

# Using a Matplotlib histogram, visualize the distribution of population across all cities. What do you observe?
df = pd.read_sql('select * from worldcities',conn)
pop1 = df.groupby('city_ascii')[['population']].sum()
plt.figure()
plt.hist(pop1.population, bins = 20)
plt.show()

# Create a bar chart with the population of the top 10 most populated countries. Which country is most populated?
pop2 = df.groupby('country')[['population']].sum().sort_values("population",ascending=False).head(10)['population']

plt.figure()
plt.bar(x = pop2.keys(), height = pop2)
plt.show()

## Given Solution ##

# 1
df = pd.read_sql('select * from worldcities',conn)
plt.figure()
plt.hist(df['population'], bins = 30) #Play around with the bin sizes when plotting your histogram
plt.show()

# 2
countries = df.groupby("country")['population'].sum().sort_values(ascending = False)
countries.head(1).index.values[0]