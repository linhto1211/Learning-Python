# Define values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  value_also_key=[]
  for key in my_dictionary.keys():
    for value in my_dictionary.values():
      if key == value:
        value_also_key.append(key)
  return value_also_key

# Check if functions work
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]
