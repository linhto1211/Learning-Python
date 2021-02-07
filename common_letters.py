def common_letters(string_one,string_two):
  common=[]
  for one in string_one:
    if (one in string_two) and not (one in common):
      common.append(one)
  return common

print(common_letters("manhattan","san francisco"))
  
