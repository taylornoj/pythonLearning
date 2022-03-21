# """
# Planning:
# - ask user for a word (get input)
# - replace section of story with users word in backend
# - repeat until all blanks are filled
# - print out final string
# """

proseString = """
Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME
"""
# print(proseString)

userInput = input("Please provide a holiday: ")

# print(proseString)
# print(userInput)

newProseString = proseString.replace("HOLIDAY", userInput)
# proseString = newProseString

print(newProseString)