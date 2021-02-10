# Define add_ten function here:
def add_ten(my_dictionary):
  for key,values in my_dictionary.items():
    values+=10
    my_dictionary.update({key:values})
  return my_dictionary

# Check if function work
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}
