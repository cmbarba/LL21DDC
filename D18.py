### Day 18 Challenge ###

## Provided ##

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./csv/thai_tourism.csv')
df.head()

## Work ##

# What kind of correlation is there between Receipts (bn $) and % of GNP?
receipts = df['Receipts (bn $)']
gdp = df['% of GNP']
plt.figure()
plt.scatter(receipts, gdp)
plt.show()

# What is the correlation coefficient between Receipts (bn $) and % of GNP?
receipts.corr(gdp)

# Which columns have the highest correlation?
nTourists = df['Number of tourists (m)']
iTourists = df['Income per tourist ($)'] #is read as str. Did LHL write in commas (e.g. "1,613")?
receipts.corr(nTourists) #<--- is the answer
receipts.corr(iTourists) #doesn't run because iTourists is read as  str
gdp.corr(nTourists)
gdp.corr(iTourists) #doesn't run because iTourists is read as  str
nTourists.corr(iTourists) #doesn't run because iTourists is read as  str

## Given Solution ##

# What kind of correlation is there between Receipts (bn $) and % of GNP?
df.corr()

# What is the correlation coefficient between Receipts (bn $) and % of GNP?
df.corr().loc['Receipts (bn $)','% of GNP']

# Which columns have the highest correlation?
corr = df.corr().replace(1,0) # we replace 1 with 0 so max() function is not affected by 1
corr.max().sort_values() # maximum is in the row with index "Receipts (bn $)"
corr['Receipts (bn $)'].idxmax()