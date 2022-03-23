# keep doubling the bacteria population for n generations
# n is the difference between the first and last number in the range

# import Pythons build in time library to put pause between each generation
import time

bacteria = "🌭"

for generation in range(0, 10):
  bacteria = bacteria + bacteria

print(bacteria)

