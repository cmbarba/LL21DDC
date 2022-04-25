## Day 14 Challenge ##

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