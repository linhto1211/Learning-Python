# Define x_length_words function:
def x_length_words(sentence,x):
  sentence_split=sentence.split(" ")
  count=0
  for index in list(range(len(sentence_split))):
    if len(sentence_split[index])>=x:
      count+=1
    else:
      count+=0
  print(count)
  if count == len(sentence_split):
    return True
  else:
    return False

# Check if function works:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
