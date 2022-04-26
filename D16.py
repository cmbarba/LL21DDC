### Day 16 Challenge ###

## Provided ##

import sqlite3
import pandas as pd
conn = sqlite3.connect("./csv/himalayas.db")

## Work ##

# How many expeditions went to the peak of Everest?
peaks = pd.read_sql('select * from peaks',conn)
exped = pd.read_sql('select * from exped',conn)
members = pd.read_sql('select * from members',conn)
everest1 = exped[exped['peakid'] == 'EVER']
print(len(everest1))

# How many people went to the peak of Everest? (One person could have gone more than once)
everest2 = pd.read_sql("""
    select E.peakid as peak,
        M.fname,
        M.lname
    from exped as E
    inner join members as M
        on E.expid = M.expid
""",conn)
total = everest2[everest2['peak'] == 'EVER']
print(len(total))

## Given Solution ##

# How many expeditions went to the peak of Everest?
len(pd.read_sql("""
    select P.pkname, 
        E.expid
    from peaks as P
    inner join exped as E
        on P.peakid = E.peakid
    where P.pkname = 'Everest'
""",conn))

# How many people went to the peak of Everest? (One person could have gone more than once)
len(pd.read_sql("""
    select P.pkname, 
        M.fname,
        M.lname,
        M.expid
    from peaks as P
    inner join members as M
        on P.peakid = M.peakid
    where P.pkname = 'Everest'
""",conn))