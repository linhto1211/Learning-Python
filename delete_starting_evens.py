#Define function
def delete_starting_evens(lst):
  index = 0
  while index < len(lst):
    if lst[index] % 2 == 0:
      lst.pop(index)
    else:
      break
  return lst    

#Check if function works:
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Answers: 
#[11, 12, 15]
#[]
