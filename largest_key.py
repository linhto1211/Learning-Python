# Define max_key function here:
def max_key(my_dictionary):
  max_value = 0
  max_key = 0
  for key, value in my_dictionary.items():
    if max_value < value:
      max_value = value
      max_key = key
  return max_key
  
# Check if function works:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
