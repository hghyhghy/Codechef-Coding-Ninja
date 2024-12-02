

#first non repeating character

def main(string):
    
    freq={}

    for char in string:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            
            
    for char in string:
        
        if freq[char] ==1:
            
            return char
        
    
    return -1
a="aDcadhc"
print(main(a))