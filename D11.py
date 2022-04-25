## Day 11 Challenge ##

# Provided

import pandas as pd
df = pd.read_csv('./csv/dubai_properties_data.csv')
df.head()

# Work

#Which neighborhood has the biggest difference between maximum and minimum property price?
df1 = df.groupby(['neighborhood']).agg({'price' : ['max','min']})
(df1['price']['max'] - df1['price']['min']).sort_values(ascending=False).head(1)

# #####################
# Solution 2
import pandas as pd
df = pd.read_csv('./csv/dubai_properties_data.csv')

# Save grouped by table into variable
difference = df.groupby(['neighborhood']).agg({'price' : 'max'}) - df.groupby(['neighborhood']).agg({'price' : 'min'})

# Sort the variable for answer
difference.sort_values(by='price', ascending=False)
