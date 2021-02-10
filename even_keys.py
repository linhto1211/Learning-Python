#Define sum_even_keys function here:
def sum_even_keys(my_dictionary):
  sum_evens=0
  for evens in my_dictionary.keys():
    if evens % 2 == 0:
      sum_evens+=my_dictionary[evens]
  return sum_evens

#Check if function works
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6
