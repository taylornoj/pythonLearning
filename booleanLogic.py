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
 