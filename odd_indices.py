#Define function
def odd_indices(lst):
  index = 0
  new_list=[]
  while index < len(lst):
    if index % 2 != 0:
      new_list.append(lst[index])
      index +=1
    else:
      index +=1
  return new_list  

#Check if function works
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Answer: [3, 10, -2]
