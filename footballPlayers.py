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