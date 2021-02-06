#Define function 
def divisible_by_ten(nums):
  nums= [num+ 1 for num in nums if num % 10 == 0]
  return len(nums)

#Check if the function works:
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Answer: 3
