## Day 14 Challenge ##

# Provided

# We will be using data that contains traffic information for New Zealand during the year 2020.
import pandas as pd
df = pd.read_csv('nz_car_traffic.csv')
df.head()

# Work

#Find the region (using variable regionName) with the lowest total amount of light (using variable classWeight) traffic, and the region with the lowest total amount of heavy (using variable classWeight) traffic
df0 = df[df['classWeight'].isin(['Light'])]
df0.groupby(['regionName'])[['trafficCount']].sum().sort_values(ascending=True,by='trafficCount').head(1)

df1 = df[df['classWeight'].isin(['Heavy'])]
df1.groupby(['regionName'])[['trafficCount']].sum().sort_values(ascending=True,by='trafficCount').head(1)

#Using a bar chart, which month had the lowest amount of total traffic in 2020?
#plots were STILL not being drawn so had to skip
df2 = df.groupby(['startDate'])[['trafficCount']].sum()
df2.trafficCount.plot(kind='bar')

#What percent of New Zealand’s traffic (using variable trafficCount) was classified as heavy (using variable classWeight) in 2020?
x = df1.trafficCount.sum()
y = df2.trafficCount.sum()
r = x/y
r