# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

def length_of_last_word(string):
    
    words=string.rstrip().split()
    
    if words:
        
        return len(words[-1])

    else:
        
        return "None"

s1 = "Hello world"
print(length_of_last_word(s1))  # Output: 5