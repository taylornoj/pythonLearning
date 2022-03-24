alphabet = 'abcdefghijklmnopqrstuvwxyz'

lphbt = alphabet # alphabet with all vowels taken out
vowels = 'aeiou'

for vowel in vowels:
  lphbt = lphbt.replace(vowel, '')

print(lphbt) # print alphabet without vowels

faveAlphabet = alphabet
favouriteLetters = 'gsbrox'

for letter in favouriteLetters:
  faveAlphabet = faveAlphabet.replace(letter, letter.upper())

print(faveAlphabet)