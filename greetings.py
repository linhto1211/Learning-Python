#Define function:
def add_greetings(names):
  greetings=["Hello, " + name for name in names ]
  return greetings
 
#Check if function works
print(add_greetings(["Owen", "Max", "Sophie"]))

#Answer: ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']
