#Define make_spoonerism function here:
def make_spoonerism(word1,word2):
  new_word1=word1.replace(word1[0],word2[0])
  new_word2=word2.replace(word2[0],word1[0])
  return new_word1 + " " + new_word2

#Check if fuction works
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
