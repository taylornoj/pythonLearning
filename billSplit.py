billTotal = float(input("Bill total: "))
tipPercent = int(input("Tip percentage: "))
numOfPeople = int(input("Number of people: "))

taxRate = 0.14
tax = billTotal * taxRate

tipAmount = billTotal * tipPercent / 100

total = round(billTotal + tax + tipPercent, 2)

totalPerPerson = round(total / numOfPeople, 2)

print("The total is: $ " + str(total))
print("Each person should pay: $" + str(totalPerPerson))