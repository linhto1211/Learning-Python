# Define count_first_letter function here:
def count_first_letter(names):
  count_first_letter={}
  for key,values in names.items():
    if key[0] not in count_first_letter:
      count_first_letter[key[0]]=0
    for value in values: 
      count_first_letter[key[0]]+=1
  return count_first_letter
    
    
# Check if function works:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
