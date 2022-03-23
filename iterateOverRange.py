# keep doubling the bacteria population for n generations
# n is the difference between the first and last number in the range

# import Pythons build in time library to put pause between each generation
import time

bacteria = "🌭"
# make no. of generations into a variable
generations = 10

for generation in range(0, generations):
  bacteria = bacteria * 2
  print(bacteria)
  # telling Python to pause and do nothing for 0.5 seconds before next instruction
  time.sleep(0.5)

