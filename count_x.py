# Define count_char_x function here:
def count_char_x(word,x):
  count=0
  for y in word:
   if y==x:
     count+=1
  return count  
  
# Check if functions work:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
