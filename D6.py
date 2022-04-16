## Day 6 Challenge ##

# Provided

a = [['w','n','N'], 'narrow']

b = [['w','n','N','W','n','W'],'wide']

c = [['w','n','n','w','n','n'], 'narrow']

# Work

def find_the_gate(spots, vehicle):
    i = 0
    for x in spots:
        if vehicle == 'narrow':
            if x =='N' or x =='W':
                print(f'Found gate for {vehicle} plane at index {i}.')
                break
        if vehicle == 'wide' and x == 'W':
            print(f'Found gate for {vehicle} plane at index {i}.')
            break
        if i == (len(spots)-1):
            print(f'No gates found for {vehicle} plane.')
        i += 1


find_the_gate(a[0],a[1])
find_the_gate(b[0],b[1])
find_the_gate(c[0],c[1])

find_the_gate(['w','n','n','w','N','n','w','N','N','w','n','n','w','n','n','W','W','W','W','n','n','w','n','n'], 'wide')

# Solution 2
def find_the_gate(spots, vehicle):
    if vehicle == 'narrow':
        for i in range(len(spots)):
            if spots[i] == 'N':
                return i
        return False
            
    elif vehicle == 'wide':
        for i in range(len(spots)):
            if spots[i] == 'W':
                return i
        return False
