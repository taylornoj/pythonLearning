dogs = ['Ellie', 'Alaska', 'Jellybean', 'Fox']
bool(dogs)
print(bool(dogs)) # True

badDogs = []
bool(badDogs)
print(bool(badDogs)) # False

dogSpeech = "Bark bark"
print(bool(dogSpeech)) # True

speechless = ""
print(bool(speechless)) # False

numberOfDogs = 45342
print(bool(numberOfDogs)) # True

cats = 0
print(bool(cats)) # False

loveDogs = True
print(bool(loveDogs)) # True

#####

roomTemp = 23
plutoSurfaceTemp = -203
question = roomTemp < plutoSurfaceTemp
print(bool(question)) # False
print(bool(roomTemp < plutoSurfaceTemp)) # False

#####

dogs = ['Ellie', 'Alaska', 'Jellybean', 'Fox']
print('Ellie in dogs?', bool('Ellie' in dogs)) # True
print('Max in dogs?', bool('Max' in dogs)) # False
 
 ## the 'is' operator compares the thing to the left and thing to the right
 ## to say, "are these the same thing?"
bestDog = dogs[0] # Can change [] to any index
print(bool(bestDog is 'Ellie')) # True
print(bool(bestDog is 'Fox')) # False

## BUT we should use == operator in place of keyword 'is'
## 'is' is more readable but has some quirks; 

#####

# Grouping expressions together using 'and' keyword
# if either side is false, whole thing is false
outsideTemp = 28
sunny = True
print("Is it over 25 and sunny?", bool(outsideTemp > 25 and sunny)) # True