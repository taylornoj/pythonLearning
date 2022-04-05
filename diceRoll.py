from random import randint
import time

repeat = True

while repeat:
  print("Rolling dice...")
  time.sleep(2)
  print("You rolled ", randint(1,6), " and ", randint(1,6))
  print("Do you want to roll again? Y/N")
  repeat = "Y" in input()

