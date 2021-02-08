letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Define function unique_english_letters here:
def unique_english_letters(word):
  count=0
  unique_letter=""
  for w in word:
    for l in letters:
      if (l==w) and not (unique_letter.find(l)>=1):   
        unique_letter+=l
        count+=1
  print(unique_letter)
  return count

# Check if function works
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
