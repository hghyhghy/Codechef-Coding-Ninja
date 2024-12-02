# You are given a string A consisting of lower case English letters. You have to find the first non-repeating character from each stream of characters.

# For Example: If the given string is 'bbaca', then the operations are done as:

# The first stream is “b” and the first non-repeating character is ‘b’ itself, so print ‘b’. 
# The next stream is “bb” and there are no non-repeating characters, so print nothing.
# The next stream is “bba” and the first non-repeating character is ‘a’, so print ‘a’. 
# The next stream is “bbac” and the first non-repeating character is ‘a’, so print ‘a’. 
# The next stream is “bbaca” and the first non-repeating character is ‘c’, so print ‘c’. 

def first_unique_char_in_string(string:str)->list[str]:
    freq={}
    order=[]
    result=[]
    
    for char in string:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            order.append(char)

    
        found=False
        for char1 in order:
            
            if freq[char1] == 1:
                
                result.append(char1)
                found=True
                break
            
        
        if not found:
            
            result.append("")

    
    return result

A = "bbaca"
print(first_unique_char_in_string(A))
        
        