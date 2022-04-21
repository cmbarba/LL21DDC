## Day 11 Challenge ##

# Provided

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')
df.head()

# Work

#Which neighborhood has the biggest difference between maximum and minimum property price?
df1 = df.groupby(['neighborhood']).agg({'price' : ['max','min']})
(df1['price']['max'] - df1['price']['min']).sort_values(ascending=False).head(1)