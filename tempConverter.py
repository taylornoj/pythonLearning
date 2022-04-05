print("Choose from the options below:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
option = int(input("Option 1 or 2: "))

if option == 1:
  celsius = float(input("Temperature in Celsius: "))
elif option == 2:
  fahrenheit = float(input("Temperature in Fahrenheit: "))
else:
  print("Choose option 1 or 2")