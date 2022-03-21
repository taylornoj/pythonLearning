# float() method returns floating point number from a number or a string
billTotal = float(input("Bill total: "))
# int() method returns an integer object from any number or string
tipPercent = int(input("Tip percentage: "))
numOfPeople = int(input("Number of people: "))

taxRate = 0.14
tax = billTotal * taxRate

tipAmount = billTotal * tipPercent / 100

total = round(billTotal + tax + tipPercent, 2)

totalPerPerson = round(total / numOfPeople, 2)

# str() used to convert specified value into a string
print("The total is: $ " + str(total))
print("Each person should pay: $" + str(totalPerPerson))