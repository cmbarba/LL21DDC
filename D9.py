## Day 9 Challenge ##

# Provided

import pandas as pd
df = pd.read_csv('wine.csv')

# Work

## How many Italian wines have a lower percentage of alcohol than 13%
len(df[df['Alcohol'] < 13])

## How many wines are there in class 3?
len(df[df['Class'] == 3])

# Stretch

## How many wines have a level of magnesium between 90 and 100?
data1 = df[df['Magnesium'] >= 90] #!!! given solution uses .between() which is inclusive of boundaries by default
data2 = data1[data1['Magnesium'] <= 100] #!!! given solution uses .between() which is inclusive of boundaries by default
len(data2)

## How many wines have a level of magnesium higher than 90, and a percentage of alcohol lower than 13.5%?
data3 = df[df['Magnesium'] > 90]
data4 = data3[data3['Alcohol'] < 13.5]
len(data4)