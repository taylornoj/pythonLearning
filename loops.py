# for loops

#  for item in colletion:
  # Do Stuff

# The : denotes that the next lines are part of a block# 
# and the indentation on line 4 is important

# instead of using { } like in JS, Python uses indentations

clothing = [
  "Shirt",
  "Pants",
  "Socks"
]

for item in clothing:
  foldedItem = "Folded " + item
  print(foldedItem)
print("This line is not part of the `for` loop")

# line 20 will only run once  lines 8 and 9 have gone through every items in 'clothing'