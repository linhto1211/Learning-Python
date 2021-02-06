#Define function
def exponents(bases,powers):
  exponents=[]  
  for base in bases:
    for power in powers:
        exponents += [base**power]
  return exponents

#Check if function works
print(exponents([2, 3, 4], [1, 2, 3]))

#Answer: [2, 4, 8, 3, 9, 27, 4, 16, 64]
