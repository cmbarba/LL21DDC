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

i = 0

for x in layout:
    if x[0]=="E":
        if x[1]=="e":
            z = [i,0]
            print(f"Seat at Row {i+1} Seat 1 (Index {(i)},0")
            break
    if x[-1]=="E":
        if x[-2]=="e":
            z = [i,-1]
            print(f"Seat at Row {i+1} Seat 11 (Index {(i)},-1)")
            break
    i +=1

# Stretch

newlayout = layout
newlayout[z[0]].insert(z[1],"O")
newlayout[z[0]].pop(z[1])
print(newlayout[z[0]])


# Other Solution
row_number = 0
available_seats = []
for row in layout:
    row_number += 1
    if row[0] == 'E' and row[1] == 'e':
        available_seats.append([f'row {row_number}', 'first seat'])
    if row[-1] == 'E' and row[-2] == 'e':
        available_seats.append([f'row {row_number}', 'last seat'])

print(available_seats) #first index should be closest seat

#stretch
layout[3].insert(-1, "O")
layout[3].pop(-1)

print(layout[3])
