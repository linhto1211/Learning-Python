# Define function check_for_name here:
def check_for_name(sentence,name):
  if (sentence.find(name) >=1) or (sentence.find(name.lower()) >=1) or sentence.find(name.upper()) >=1 :
    return True
  else:
    return False

# Check if your functions work:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False
