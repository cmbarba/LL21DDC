## Day 12 Challenge ##

# Provided

import pandas as pd
df = pd.read_csv('aus_weather.csv')

# Work

d1 = df[df['season'].isin('summer','winter')] #originally used .str.contains('winter|summer') instead of .isin()
d2 = d1.groupby(['Location','season']).agg({'Temp9am' : 'mean'}).unstack(level=1)
(d2['Temp9am']['summer'] - d2['Temp9am']['winter'])