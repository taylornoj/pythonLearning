subtotal = float(input("What is the subtotal? "))



tax = 0.25

tax = subtotal * tax
total = subtotal + tax
print("The amount of tax owed is: $" + str(tax))
print("Your total bill is: $" + str(total))