## Day 15 Challenge ##

# Provided

import sqlite3
import pandas as pd
conn = sqlite3.connect("himalayas.db")

# Work

#How many peaks are higher than 8000 metres?
peaks = pd.read_sql('select * from peaks',conn)
len(peaks[peaks['heightm'] > 8000])

#How many women (sex = 'F') were part of the expeditions?
females = pd.read_sql("""
            SELECT fname,
                lname,
                sex
            FROM members
            WHERE sex = 'F'
            """
            ,conn)
len(females)


###############
# Solution 2

import sqlite3
import pandas as pd
conn = sqlite3.connect("himalayas.db")


# How to actually locate the tables data available 
cur = conn.cursor()
cur.execute('SELECT name FROM sqlite_master WHERE type = "table"').fetchall()
# [('peaks',), ('members',), ('exped',)] <-- These are the tables we can get data from

# Question 1
peaks = pd.read_sql('select * from peaks where heightm > 8000', conn)
print(len(peaks))

# Question 2
members = pd.read_sql('select * from members where sex == "F"', conn)
print(len(members))
