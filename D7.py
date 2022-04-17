## Day 7 Challenge ##

# Provided

# import pandas as pd
# import statistics
# df = pd.read_csv('fc_barcelona.csv')
# df.head()

# points = df.Pts
# games_played = df.MP
# wins = df.W
# losses = df.L
# attendance = df.Attendance.dropna() # skipping missing values (NaN) because there were no fans during 2020-2021 season because of COVID

# Work

print(f"Max games played in one season: {max(games_played)}")
print(f"Average attendance across all seasons: {sum(attendance)/len(attendance)}")
print(f"Difference between median value of wins and losses: {statistics.median(wins)-statistics.median(losses)}")
print(f"Minimum wins in one season: {min(wins)}")
print(f"Different between max and min points across all seasons: {max(points)-min(points)}")