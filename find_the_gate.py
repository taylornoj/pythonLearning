def find_the_gate(spots, vehicle):
  for i in range(len(spots)):
    if spots[i] == str(vehicle[0]):
      return spots[i]
    else:
      return False
  return "Number does not exist"

print(find_the_gate(
  ['w','n','n','w','N','n','w','N','N','w','n','n','w','n','n','W','W','W','W','n','n','w','n','n'], 'wide'
))