## Day 3 Challenge ##

# Provided

from turtle import clear


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

l1 = len(layout)
#print(l1)
l2 = len(layout[0])
#print(l2)

i = 0
while i < l1:
    j = 0
    while j < (l2-1):
        #print(f"[i,j] = [{i},{j}]")
        if layout[i][j] == "E":
            if layout[i][(j+1)] =="e":
                print(f"Seat at [{i},{j}]")
        elif layout[i][j] =="e":
            if layout[i][(j+1)] =="E":
                print(f"Seat at [{i},{j}]")            
        j+=1
    i+=1
