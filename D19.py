### Day 19 Challenge ###

## Provided ##

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./csv/air_traffic_data.csv')
df.head()

## Work ##

# What is the origin city (using variable ORIGIN_CITY_NAME) with the highest total number of passengers who travelled to Vancouver?
df[df.DEST == 'YVR'].groupby(['ORIGIN_CITY_NAME']).agg({'PASSENGERS' : 'sum'}).sort_values(ascending=False,by='PASSENGERS').head(1)

# According to our data, how many passengers travelled from that origin city to Vancouver?
#Use output from above

# Use a histogram to plot the probability distribution of distances for all routes in June 2021.
#Not required to submit answer
plt.figure()
plt.hist(df['DISTANCE'], bins = 40)
plt.show()

## Given Solution ##

# 1. and 2.
df_van = df[df.DEST_CITY_NAME.str.contains("Vancouver")]
df_van.groupby('ORIGIN_CITY_NAME')[['PASSENGERS']].sum().sort_values("PASSENGERS",ascending=False).head()

# 3.
plt.figure()
plt.hist(df[df['MONTH'] == 6]['DISTANCE'], bins = 30) #Play around with the bin sizes when plotting your histogram
plt.show()