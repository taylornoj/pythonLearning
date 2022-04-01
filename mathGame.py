questions = [
  [4, 3],
  [12, 34],
  [23, 10],
  [11, 32]
]

score = 0

for a, b in questions:
  response = int(input("What is the value of " + str(a) + " + " + str(b) + "? "))
  if response == a + b:
    print("Correct!")