# You are given a string 'STR' of lowercase English alphabets. You need to find the repeated character present first in the string.

# Example:
# If the string is: “abccba”, then the first repeated character is ‘c’, but the repeated character that is present first in the string is ‘a’. You need to print ‘a’.
# Note:
# Keep in mind that you need to print the repeated character that is present first in the string and not the first repeating character.

def first_repeatative(string:str)->str:
    
    freq={}
    order=[]

    for char in string:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            
            order.append(char)

    
    for char in order:
        
        if freq[char] > 1:
            
            return char
        
    
    return None

STR = "abccba"
print(first_repeatative(STR))
 