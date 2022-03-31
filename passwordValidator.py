createdPassword = input("Create a password: ")
confirmedPassword = input("Re enter password: ")

if createdPassword != confirmedPassword:
  print("Passwords do not match")
elif len(createdPassword) < 8:
  print("Password must be at least 8 characters long")
else:
  print("Password confirmed")