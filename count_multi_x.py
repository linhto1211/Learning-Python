# Define count_multi_char_x function here:
def count_multi_char_x(word,x):
    split=word.split(x)
    print(split)
    return len(split)-1
    

# Check if function works
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
