instructionSteps = [
  "turn left",
  "go straight",
  "turn right",
  "keep going until you see a statue",
  "turn right",
  "turn right again",
  "park on the sidewalk"
]

instructions = "First, "

for nextInstruction in instructionSteps:
  instructions = instructions + nextInstruction + ", then "

print(instructions + "you're there!")