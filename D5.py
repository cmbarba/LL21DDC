## Day 5 Challenge ##

# Provided

# dictionary where 
landmarks = {
    "Big Ben": 12,
    "Tower Bridge": 25,
    "Buckingham Palace": 15,
    "Madame Tussauds": 25,
    "London Eye": 40,
    "Tower of London": 25,
    "Emirates Air Line cable car": 16,
    "London Transport Museum": 7,
    "Wembley Stadium": 8,
    "Hyde Park": 0,
    "The View from The Shard": 14
}

# Work

places = []

for x,y in landmarks.items(): #items() gives access to both keys and values, otherwise just keys
    print(x,y)
    if y < 15:
        places.append([x,y])

print(places)


# Other solution

# store landmark destinations with wait times < 15min
destinations = []

# loop for landmarks times
for landmark in landmarks:
    x = landmarks.get(landmark, "not found")
    if x < 15:
        destinations.append(landmark)
    

print(destinations)
