user_input = str(input("Enter a Phrase: "))
text = user_input.split()
acronym = " "

for i in text:
  acronym = acronym + str(i[0]).upper()
print(acronym)

# 'best friend forever' prints BFF
# 'artificial intelligence' prints AI