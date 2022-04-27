### Day 17 Challenge ###

## Provided ##

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('toyota_cars.csv')

## Work ##

# What were the two most popular Toyota vehicle categories in 2020?
df = pd.read_csv('toyota_cars.csv')
data = df[df['Year'] == 2020].groupby(['Category'])[['Make']].count().sort_values(ascending=True,by='Make').tail(5)
pop = data['Make']

plt.figure()
plt.bar(x = pop.keys(), height = pop)
plt.title("Top 5 Most Popular Toyota Cars in 2020")
plt.show()

## Given Solution ##

df = df[df.Year == 2020]
grouped_df = df.groupby('Category').size()

plt.figure()
plt.bar(x = grouped_df.index, height = grouped_df.values)
plt.show()