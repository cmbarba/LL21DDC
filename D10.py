## Day 10 Challenge ##

# Provided

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')

# Work

#Which neighborhood has the highest average property price(?)...
df.groupby(['neighborhood'])[['price']].mean().sort_values(ascending=False,by='price').head()

#...and the highest (average) size_in_sqft? ->poor wording by LHL excludes 'average' and ends up implying max
df.groupby(['neighborhood'])[['size_in_sqft']].mean().sort_values(ascending=False,by='size_in_sqft').head()