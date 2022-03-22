from cgi import test


todo = [
  "Buy groceries",
  "Get haircut",
  "Do laundry",
  "Write in journal"
]

print(todo)
# places "Wash car" at end
todo.append("Wash car")
print(todo) 

# places "Clean kitchen" in index 1
todo.insert(1, "Clean kitchen")
print(todo)

# changes "Buy groceries" to "Unload groceries"
todo[0] = "Unload groceries"
print(todo)

# make a second list and...
tomorrowsTodo = [
  "Walk dog",
  "Clean garden",
  "Call friend",
  "Put away laundry"
]

# add it to original list to print everything together
todo = todo + tomorrowsTodo

print(todo)