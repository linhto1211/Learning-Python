#Define function
def larger_sum(lst1,lst2):
  larger_sum=0
  sum_lst1=0
  sum_lst2=0
  for lst_1 in lst1:
    sum_lst1+=lst_1
  for lst_2 in lst2:
    sum_lst2+=lst_2
  print(sum_lst1)
  print(sum_lst2)
  if sum_lst2 <=sum_lst1:
    return lst1
  else:
    return lst2

#Check if function works
print(larger_sum([1, 9, 5], [2, 3, 11]))

#Answer: 
#15
#16
#[2, 3, 11]
