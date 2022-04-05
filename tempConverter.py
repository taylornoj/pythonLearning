print("Choose from the options below:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
option = int(input("Option 1 or 2: "))

if option == 1:
  celsius = float(input("Temperature in Celsius: "))
  fahrenheit = 1.8 * (celsius) + 32.0
  fahrenheit = round(fahrenheit, 1) # f temp rounded to one decimal place
  print("Temperature in Fahrenheit: ", fahrenheit)
elif option == 2:
  fahrenheit = float(input("Temperature in Fahrenheit: "))
  celsius = (fahrenheit - 32) / 1.8
  celsius = round(celsius,1)
  print("Temperature in Celsius: ", celsius)
else:
  print("Choose option 1 or 2")