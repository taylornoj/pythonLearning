cartons = [
  ["Not almond milk", "Wrong logo"],
  ["Not almond milk", "Wrong logo"],
  ["Almond milk", "Wrong logo"],
  ["Almond milk", "Right logo"],
  ["Almond milk", "Wrong logo"],
]

cart = []

for carton in cartons:
  typeOfMilk = carton[0]
  logo = carton[1]
  # logic branch - 'if' followed by a compound expression
  if typeOfMilk is "Almond milk" and logo is "Right logo":
    cart.append(carton)
    break
# alternative branch
if len(cart) is 0:
  cart.append("Beer")