#Define function
def over_nine_thousand(lst):
  total_sum=0
  index=0
  while index < len(lst):
    total_sum+=lst[index]
    if total_sum==0:
      return 0
    elif total_sum>9000:
      return total_sum
    else: 
      index+=1
  return total_sum

#Check in function works
print(over_nine_thousand([8000, 900, 120, 5000]))

#Answer: 9020
