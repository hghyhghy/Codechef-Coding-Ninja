# Problem statement
# You have been given a string ‘S’.



# You must return the string ‘S’ sorted in decreasing order based on the frequency of characters.

# If there are multiple answers, return any of them.

def sort_char_by_freq(string:str)->str:
    
    freq={}

    for char in string:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            
    new_char=sorted(freq, key=lambda x:(-freq[x],x) )
    
    result=[]
    for char in new_char:
        
        result.extend([char]*freq[char])

    return "".join(result)

a="abAb"
print(sort_char_by_freq(a))