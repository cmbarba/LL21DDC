## Day 3 Challenge ##

# Provided

layout = [
    ["O","e","e",None, "e","o","e",None, "o","o","E"], # row 1
    ["O","o","e",None, "e","o","e",None, "e","o","E"], # row 2
    ["O","o","o",None, "o","o","e",None, "o","e","O"], # row 3
    ["E","o","e",None, "e","o","e",None, "o","e","E"], # row 4 
    ["E","e","o",None, "e","e","e",None, "o","o","E"], # row 5
    ["O","e","e",None, "e","e","e",None, "e","e","E"]  # row 6
]

# Work

#Conditions are consecutive E,e or e,E

i = 1

for x in layout:
    if x[0]=="E":
        if x[1]=="e":
            print(f"Seat at Row {i} Seat 1 (Index {(i-1)},0")
            break
    if x[-1]=="E":
        if x[-2]=="e":
            print(f"Seat at Row {i} Seat 11 (Index {(i-1)},-1)")
            break
    i +=1