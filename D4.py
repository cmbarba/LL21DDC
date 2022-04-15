## Day 4 Challenge ##

# Provided

starters = {
    "Potato Pancakes": 7.99,
    "Salami Platter": 10.29,
    "Brezel": 6.99,
    "Maultaschen": 9.99,
    "Fried Potatoes": 4.99
}

mains = {
    "Braised Beef Short Ribs": 18.99,
    "Paprika Beef Goulash": 15.5,
    "Jager Schnitzel": 16.99,
    "House-mase Bratwurst": 11.99,
    "Kasespatzle": 14.99,
    "German Ravioli": 12.79,
    "Curry Wurst": 10.99
}

desserts = {
    "Chilled Chocolate Fondant": 7.9,
    "Pepermint Crisp Tart": 5.9,
    "Ginger Cobbler": 6.9,
}

beers = {
    "Stigel Radler": 6.9,
    "Munich Lager": 7.9,
    "Kong Ludwig Weissbier": 8.9,
    "Warsteiner Punkel": 7.5,
}

# if you want to see the keys of the dictionary in the list: keys = list(starters.keys())
# if you want to see the keys of the dictionary in the list: values = list(starters.values())

# Work

meals = {
    "Starters": list(starters.keys()),
    "Mains": list(mains.keys()),
    "Desserts": list(desserts.keys()),
    "Beers": list(beers.keys()),
}

print(meals)

total = max(starters.values()) + max(mains.values()) + max(desserts.values()) + max(beers.values())
tip = total * 0.1
print(tip)


# Solution 2
# data
meals = {
    "starters": starters.items(),
    "mains": mains.items(),
    "desserts": desserts.items(),
    "beers": beers.items()
}

# variables
bill = []
totals_list = []

# function
def update_bill(list):
    list.sort()
    totals_list.append(list[-1])
    bill.clear()

    
# Find the most expensive meals
for price in meals["starters"]: 
    bill.append(price[1])    
update_bill(bill)

for price in meals["mains"]: 
    bill.append(price[1])    
update_bill(bill)

for price in meals["desserts"]: 
    bill.append(price[1])    
update_bill(bill)

for price in meals["beers"]: 
    bill.append(price[1])    
update_bill(bill)

print(totals_list) # [10.29, 18.99, 7.9, 8.9]

# Sum of meal
total = 0
for cost in totals_list:
    total += cost

#Calculate tip
final = total * 0.10
print(final) # 4.608
