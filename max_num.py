#Define function
def max_num(nums):
  max_num=nums[0]
  index= 0
  for index in list(range(len(nums))):
    if nums[index] > max_num:
      max_num=nums[index]
      index+=1
    elif nums[index] < max_num:
      index+=1
  return max_num

#Check if function works
print(max_num([50, -10, 0, 75, 20]))  

#Answer: 75
