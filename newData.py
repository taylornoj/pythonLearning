instructionSteps = [
  "turn left",
  "go straight",
  "turn right",
  "keep going until you see a statue",
  "turn right",
  "turn right again",
  "park on the sidewalk"
]

# instructions = "First, "

# for nextInstruction in instructionSteps:
#   instructions = instructions + nextInstruction + ", then "

# print(instructions + "you're there!")


for nextInstruction in instructionSteps:
  instructionStepsButScreamed = []
  upperInstruction = nextInstruction.upper()
  instructionStepsButScreamed.append(upperInstruction)

print(instructionStepsButScreamed) # whole list in caps

print(upperInstruction) # PARK ON THE SIDEWALK

# when instructionStepsButScreamed = [] is in the for loop // ['PARK ON THE SIDEWALK']