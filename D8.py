## Day 8 Challenge ##

# Provided

import pandas as pd

df = pd.read_csv('paris_landmarks.csv')

# Work

df.sort_values(by="price",ascending=False).head()
df["queue_time"].mean()