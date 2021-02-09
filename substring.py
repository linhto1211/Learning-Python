# Define function here:
def substring_between_letters(word,start,end):
  find_start=word.find(start)
  find_end=word.find(end)
  if (find_start == -1) or (find_end ==-1):
    return word
  else:
    return word[find_start+1:find_end]
    
# Check if function work:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
