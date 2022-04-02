# """
# Planning:
# - ask user for a word (get input)
# - replace section of story with users word in backend
# - repeat until all blanks are filled
# - print out final string
# """

letterHome = [
  # Title
  "A Letter Home",

  # Prose String
  """
  Hi mom,

  Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to 
  COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY 
  is the best place in the world to build a career around them. I'll need to start 
  small-- At first, all I'll be allowed to do is to VERB near them, but when people 
  see how ADJECTIVE I can be, I'm sure to rise to the top.

  Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be 
  sure to call every HOLIDAY.

  Love,

  NAME
  """,

  # Replacements
  [
    ["Please provide an occupation: ", "OCCUPATION"],
    ["Please provide a country: ", "COUNTRY"],
    ["Please provide a plural noun: ", "PLURAL_NOUN"],
    ["Please provide a verb: ", "VERB"],
    ["Please provide an adjective: ", "ADJECTIVE"],
    ["Please provide a personal item: ", "PERSONAL_ITEM"],
    ["Please provide a holiday: ", "HOLIDAY"],
    ["Please provide your name: ", "NAME"],
  ]
]

sale = [
  # Title
  "A Great Sale",

  # Prose String
  """
  SALE SALE SALE

  Today only: Buy NUMBER PLURAL_NOUN and get a free NOUN!

  Sign up for our exclisive METAL card and receive 50% off of your first purchase!
  """,

  # Replacements
  [
    ["Please provide a number: ", "NUMBER"],
    ["Please provide a plural noun: ", "PLURAL_NOUN"],
    ["Please provide a noun: ", "NOUN"]
    ["Please provide a type of metal", "METAL"]
  ]
]



for prompt, placeholder in replacements:
  userInput = input(prompt)
  proseString = proseString.replace(placeholder, userInput)

print(proseString)