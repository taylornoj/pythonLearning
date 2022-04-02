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
    score += 1
  else:
    print("Wrongo!")

if score > len(questions) / 2:
  # len() method returns length of the list/string, etc iterable data format in Python
  print("Great job! Your score is: " + str(score) + " out of " + str(len(questions)))
else:
  print("Womp Womp! Your score is: " + str(score) + " out of " + str(len(questions)) + ". Try again!")