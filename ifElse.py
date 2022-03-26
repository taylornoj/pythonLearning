cartons = [
  ["Not almond milk", "Wrong logo"],
  ["Not almond milk", "Wrong logo"],
  ["Almond milk", "Wrong logo"],
  ["Almond milk", "Right logo"],
  ["Almond milk", "Wrong logo"],
]

cart = []
wrongCartonsLookedAt = 0

for carton in cartons:
  typeOfMilk = carton[0]
  logo = carton[1]
  # logic branch - 'if' followed by a compound expression
  if typeOfMilk == "Almond milk" and logo == "Right logo":
    cart.append(carton)
    break
  else:
    wrongCartonsLookedAt += 1
# alternative branch
if len(cart) == 0:
  cart.append("Beer")

print("I looked at " + str(wrongCartonsLookedAt) + " cartons that were not almond-painted-like-a-cow branch almond milk.")