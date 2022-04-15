# Create a new dictionary called meals that will contain the names of the courses as the keys (starters, mains...), and the name of the food or drink item as the values

# Dictionary meals should have 4 values and 4 keys: starters, mains, desserts and beers. Sum the prices of these 4 meals and multiply by 0.1.

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


meals = {
  "starters": 10.29,
  "mains": 18.99,
  "desserts": 7.9,
  "beers": 8.9
}


max_starter = max(starters,key=starters.get)
print(max_starter)

max_main = max(mains,key=mains.get)
print(max_main)

max_dessert = max(desserts,key=desserts.get)
print(max_dessert)

max_beer = max(beers,key=beers.get)
print(max_beer)

print(sum(meals.values())*0.1)