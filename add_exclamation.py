# Define function here:
def add_exclamation (word):
  if len(word) >= 20:
    return word
  while len(word) < 20:
    word+="!" 
  else: 
    return word

# Check if function works:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
