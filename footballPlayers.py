from xxlimited import foo


footballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]

# 1. get median player ---
# find number of players total:
print(len(footballers))
# find median
median = len(footballers) // 2
print(footballers[median])

# 2. get 5 players in middle of league ---
print(footballers[median-2:median+3])

# 3. Add 'Average Player' to middle of the list
footballers.insert(median, "Average Player")
print(footballers[median])

# 4. Find and change "Average Player" to all upper case
averagePlayerCaps = footballers.index("Average Player")
footballers[averagePlayerCaps] = footballers[averagePlayerCaps].upper()
print(footballers[median])

# 5. Add 5 more players to bottom of the list
footballers += [
  "Steve", "Taylor", "Ellie", "Louis", "Steph"
]
print(footballers)

# 6. AVERAGE PLAYER is no longer in the middle - fix it!
# delete AVERAGE PLAYER 
del footballers[footballers.index("AVERAGE PLAYER")]
# create new median
median = len(footballers) // 2
# insert AVERAGE PLAYER AGAIN
footballers.insert(median, "AVERAGE PLAYER")
print(footballers)