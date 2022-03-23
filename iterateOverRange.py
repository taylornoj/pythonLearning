# keep doubling the bacteria population for n generations
# n is the difference between the first and last number in the range

# import Pythons build in time library to put pause between each generation
import time

bacteria = "🌭"
# make no. of generations into a variable
generations = 10

for generation in range(0, 10):
  bacteria = bacteria + bacteria

print(bacteria)

